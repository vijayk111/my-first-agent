import asyncio
import httpx

API_URL="https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "sparkline": False
}

async def fetch_crypto_data():
    # Use 'async with' to properly close the connection when done
    async with httpx.AsyncClient() as client:
        print("--- Fetching Live Market Data ---")
        try: 
            response= await client.get(API_URL, params=PARAMS)
            #Raise an error if the request failed (4xx or 5xx)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            print(f" X API Error: {e}")
            return []

async def main():
    # Fetch the data
    raw_data= await fetch_crypto_data()

    if not raw_data:
        return
    
    expensive_coins= [
        {
            "name": coin["name"],
            "price": coin["current_price"],
            "change": coin["price_change_percentage_24h"]>100
        }
        for coin in raw_data if coin["current_price"]>100
    ]

    print(f"\n Found {len(expensive_coins)} coins worth over $100:\n")
    print(f"{'NAME':<15} | {'PRICE (USD)':<12} | {'24H CHANGE'}")
    print("-" * 45)

    for coin in expensive_coins:
        name = coin["name"]
        price=f"${coin["price"]:,.2f}"
        change=f"{coin["change"]:,.2f}%"

        print(f"{name:<15} | {price:<12} | {change}")


if __name__=="__main__":
    asyncio.run(main())