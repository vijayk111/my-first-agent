# import asyncio

# print("Testing----This is before main")

# async def say_hello():
#     print("Fetching data...")
#     await asyncio.sleep(2)
#     print("Done!")


# if __name__ == "__main__":
#     asyncio.run(say_hello())

# import asyncio
# import time

# async def fetch_api(name, delay):
#     print(f" [~]Starting fetch fro {name}")
#     await asyncio.sleep(delay)
#     print(f" [+] {name} finished after {delay}s")
#     return {"source": name, "data": "success"}

# async def main():
#     start_time = time.perf_counter()

#     #Schedule three tasks to run concurrently
#     results = await asyncio.gather(
#         fetch_api("UserDB", 1),
#         fetch_api("ProductAPI", 2),
#         fetch_api("AuthService", 1.5)
#     )

#     end_time = time.perf_counter()
#     print(f"\nAll tasks finished in {end_time - start_time:.2f} seconds")
#     print(f"Results: {results}")

# if __name__=="__main__":
#     asyncio.run(main())

import asyncio
import random

async def check_service(service_name: str):
    "Simulates checking a system service status."
    wait_time = random.uniform(0.5, 2.0)
    await asyncio.sleep(wait_time)

    #Simulate a 20% chance of failure
    status = "OK" if random.random() > 0.2 else "ERROR"
    return {service_name: status}

async def run_diagnostics():
    services = ["Nginx", "PostgreSQL", "Redis", "Docker", "SSH"]

    print("---Starting System Diagnostics---")

    tasks=[check_service(s) for s in services]

    results= await asyncio.gather(*tasks)

    print("\n---Diagnostic Report---")
    for r in results:
        for name, status in r.items():
            print(f"{name:12}: {status}")

if __name__ == "__main__":
    asyncio.run(run_diagnostics())
