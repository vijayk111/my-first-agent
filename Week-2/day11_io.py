import json
from pathlib import Path
from pydantic import BaseModel
from datetime import datetime

class AgentOutput(BaseModel):
    timestamp: str
    instruction: str
    summary: str
    status: str

instruction_file = Path("instructions.txt")
output_file = Path("agent_log.json")

if not instruction_file.exists():
    instruction_file.write_text("Analyze the current status of the Ubuntu server.")

def run_agent():
    instruction= instruction_file.read_text()
    print(f"📖 Reading instruction: {instruction}")

    summary= f"Processed at {datetime.now()}: System is healthy!"

    result = AgentOutput(
        timestamp=str(datetime.now()),
        instruction=instruction,
        summary=summary,
        status="Completed"
    )

    with open("agent_log.json", "w") as f:
        json.dump(result.model_dump(), f, indent=4)

    print(f"✅ Result saved to {output_file}")

if __name__ == "__main__":
    run_agent()