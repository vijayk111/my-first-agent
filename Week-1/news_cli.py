import asyncio
import httpx
import os
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

#Configuration
API_KEY=os.getenv("NEWS_API_KEY")

# --- ADD A SECURITY CHECK ---
if not API_KEY:
    print("❌ ERROR: NEWS_API_KEY not found in environment!")
    print("Please create a .env file with: NEWS_API_KEY=your_key")
    exit(1)

BASE_URL = "https://newsapi.org/v2/top-headlines"

#Dictonary mapping for user-friendly selection
COUNTRIES={
    "1": {"name": "USA", "code": "us"},
    "2": {"name": "India", "code": "in"},
    "3": {"name": "UK", "code": "gb"},
    "4": {"name": "Canada", "code": "ca"},
    "5": {"name": "Australia", "code": "au"}
}

async def fetch_news(country_code: str):
    params= {
        "country": country_code,
        "apiKey": API_KEY,
        "pageSize": 10
    }

    async with httpx.AsyncClient() as client: 
        print(f"\n[~] Fetching latest news...")
        response = await client.get(BASE_URL, params=params)

        if response.status_code == 401:
            return "Error: Invalid API Key. Check your config!"
        
        response.raise_for_status()
        return response.json()
    
async def main():
    print("--- Ubuntu News Tracker ---")
    for key, info in COUNTRIES.items():
        print(f"{key}. {info["name"]}")

    choice = input("\nSelect a country number: ")

    #Validate: Check if choice exits in our dict
    if choice not in COUNTRIES:
        print(f"❌ Invalid Selection. Exiting!")
        return
    
    selected_country=COUNTRIES[choice]
    data= await fetch_news(selected_country["code"])

    if isinstance(data, str): #Handle our custom error string
        print(data)
        return
    
    articles = [
        {
            "title": a["title"],
            "source": a['source']['name'],
            "url": a["url"]
        }
        for a in data.get("articles", []) 
        if a["title"] and "[Removed]" not in a["title"]
    ]

    print(f"\n --- Top Stories in {selected_country["name"]} ---")

    for i, art in enumerate(articles, 1):
        print(f"{i}. {art['title']}")
        print(f"  Source: { art['source']}")
        print(f"  Link: {art['url']} \n")


if __name__=="__main__":
    asyncio.run(main())
