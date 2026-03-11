from pydantic import BaseModel, ValidationError
from typing import List

# 1. Define the schema
class UserProfile(BaseModel):
    id:int
    username: str
    bio: str = "No bio provided"
    skills: List[str]

# 2. Simulating a list of data where some items are "broken"
raw_data= [
    {"id": 1, "username": "tux_fan", "skills": ["linux", "python"]}, # Valid
    {"id": "2", "username": "ai_dev", "skills": ["pytorch"]}, # Valid (id will be coerced)
    {"id": 3, "username": "broken_user"} # Invalid (missing skills)
]

print("--- 🛡️ Pydantic Validation Results ---")

valid_users= []

for item in raw_data:
    try:
        user= UserProfile(**item)
        valid_users.append(user)
        print(f"✅ Validated: {user.username}")
    except ValidationError as e:
        print(f"❌ Failed: {item.get('username', 'Unknown')}")
        print(e.json()) # You can see exactly what went wrong!

print(f"\n Final count of clean users: {len(valid_users)}")

"""
Why this is a "Primitive" for AI Engineering
* JSON Output: Most LLMs can be told to "Return JSON that matches this schema." You can generate that schema instantly using UserProfile.model_json_schema().
* Safety: If the AI hallucinates and forgets a required field, your code won't crash later with a KeyError; it crashes immediately at the gate with a helpful message.
* IDE Support: Now, when you type user. in VS Code, it will suggest id, username, and bio with perfect accuracy.
"""