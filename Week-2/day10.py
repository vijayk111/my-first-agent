import json
from typing import List

from pydantic import BaseModel


class Author(BaseModel):
    name: str
    twitter_handle: str

class Article(BaseModel):
    title: str
    authors: Author
    citations: List[Author]

"""
Every Pydantic model has a method called .model_json_schema(). 
This generates a standard-compliant JSON description of your code 
that you can paste directly into a prompt for Gemini, GPT, or Claude.
"""

# Generate the schema
schema= Article.model_json_schema()

print(json.dumps(schema, indent=2))