from pydantic import BaseModel, Field
from typing import List, Optional

class NewsArticle(BaseModel):
    # Required fields
    title: str
    content: str

    # Optional field with a default
    author: str= "Vijay"

    # Advanced: Validation and Meta-data
    # 'Field' lets us add descriptions or contraints (like min_length)
    tags: List[str] = Field(default_factory=list)
    word_count: Optional[int] = None

# Simulating a messy response from an AI
raw_ai_output = {
    "title": "pydantic is awesome",
    "content": "It validates my data automatically.",
    "word_count": "35", # Note: This is a string, but the model wants an int!
    "tags": ["python", "validation"]
}

# Parse it
article= NewsArticle(**raw_ai_output)

print(article.title.title())
print(type(article.word_count))

# print(article)