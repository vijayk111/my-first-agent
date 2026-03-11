from typing import Dict, List

# 1. Define a complex type hint for an 'Article'
# It's a dictionary with string keys and values that are strings, ints, or lists
ArticleData= Dict[str, str| int | List[str]]

def format_ai_summary(title: str, tags: List[str], word_count: int) -> ArticleData:
    """
    Simulates taking structured data from an AI 
    and ensuring it fits a specific format.
    """
    return {
        "name": title.title(),
        "tags": [t.lower() for t in tags],
        "length": word_count,
        "is_long_form": word_count > 500
    }

# Test it
news_summary = format_ai_summary(
    title="ai is taking over ubuntu",
    tags=["Linux", "PYTHON", "AI"],
    word_count=750
)

print(f"Structured Article: {news_summary}")
print(f"First Tag: {news_summary['tags'][0]}")