import json
from pydantic import BaseModel, Field
from typing import List

# 1. Sub-model for sources
class Source(BaseModel):
    site_name: str
    url: str
    reliability_score: float = Field(..., ge=0, le=1) # Must be between 0 and 1

# 2. Main Report Model
class ResearchReport(BaseModel):
    topic: str
    summary: str = Field(description= "A 3-sentence summary of the findings")
    key_takeaways: List[str] = Field(min_length=3)
    sources: List[Source]

# 3. Generating the "Prompt Instructions"
def get_ai_instructions():
    schema= ResearchReport.model_json_schema()

    # In real app, we send this string to the LLM
    prompt=f"""
    Please research the topic provided.
    Your output MUST be valid JSON and strictly follow this schema:
    {json.dumps(schema, indent=2)}
    """
    return prompt

# 4. Simulating a response from the AI
ai_response_json = {
    "topic": "Ubuntu 24.04 Features",
    "summary": "Noble Numbat brings GNOME 46 and a new installer.",
    "key_takeaways": ["New installer", "GNOME 46", "Netplan by default"],
    "sources": [
        {"site_name": "OMG! Ubuntu", "url": "https://omgubuntu.co.uk", "reliability_score": 0.9},
    ]
}

# 5. Validate the AI's "Vibes" into "Strict Code"
report = ResearchReport(**ai_response_json)

print(f"Report Topic: {report.topic}")
print(f"Report Summary: {report.summary}")
print(f"First Source: {report.sources[0].site_name}({report.sources[0].url})")