from typing import Dict, List, Optional, Union

# This information takes a list of strings and returns a dictionary
def process_ai_response(raw_output: List[str])->Dict[str, int]:
    return {name: len(name) for name in raw_output}

# Optional: Useful when an AI might fail to return a specific field
def get_user_bio(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "AI Enthusiast"
    return None #If it's not 1, we return None (perfectly valid for Optional)

# Updated declerations
# Old: Union[str, int] -> New: str | int
# Old: Optional[str] -> New: str | None

def main():
    print("Fetch AI Repsonse:")
    result_dict= process_ai_response(["gemini", "gpt"])
    for key, value in result_dict.items():
        print(f"{key} -> {value}")
    
    print("\nFetch User Bio:")
    print(f"User is : {get_user_bio(1)}")

if __name__=="__main__":
    main()