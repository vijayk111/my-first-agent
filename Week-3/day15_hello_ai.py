import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

def ask_ai(prompt: str):
    print(f"Querying Gemini-3.0 Flash Preview...")

    print(f"Sending prompt: {prompt}")

    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are senior expert. Provide only the terminal command and a one-sentence explanation."
        )
    )

    print("\n---AI Response---")
    print(response.text)

if __name__ == "__main__":
    user_input = "Explain why 'uv' is faster than 'pip' in three bullet points."
    ask_ai(user_input)

'''
Response before adding config in client.models.generate_content:
Querying Gemini-3.0 Flash Preview...:

Querying Gemini-3.0 Flash Preview...
Sending prompt: Explain why 'uv' is faster than 'pip' in three bullet points.

---AI Response---
Here are three key reasons why `uv` is faster than `pip`:

*   **Native Rust Implementation:** While `pip` is written in Python and limited by the speed of the Python interpreter, `uv` is built from the ground up in Rust. This allows for low-level performance optimizations and true multi-threading that Python cannot achieve.
*   **Advanced Dependency Resolution:** `uv` uses a highly optimized resolution algorithm (PubGrub) that performs dependency lookups in parallel. It can evaluate version constraints and resolve complex dependency trees significantly faster than `pip`’s single-threaded approach.
*   **Efficient Caching and Linking:** `uv` utilizes a global, content-addressable cache. Instead of re-downloading or re-copying files for every new environment, it uses "hard links" or "reflinks" to point to existing files on your disk, making the installation of previously downloaded packages nearly instantaneous.

'''

'''
Response after adding config in client.models.generate_content:

Querying Gemini-3.0 Flash Preview...
Sending prompt: Explain why 'uv' is faster than 'pip' in three bullet points.

---AI Response---
`uv pip install -r requirements.txt`

Written in Rust, `uv` significantly outperforms `pip` by leveraging a global content-addressed cache, a highly optimized parallel dependency resolver, and lazy-loading techniques.

'''