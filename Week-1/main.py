# tools=["ls", "mkdir", "cd", "uv"]
# for tool in tools:
#     print(tool)

# user={
#     "username": "vijay",
#     "level":3,
#     "is_online": True
# }

# print(user['username'])

# for key,value in user.items():
#     print(f"The {key} is {value}")

# print(" ---------------------------------------------- ")

# distros=["ubuntu", "fedora", "Debain"]
# print(distros)
# distros.append("Arch")
# print(distros)

# my_os={
#     "name": distros[0],
#     "version": "24.04",
#     "is_lts": True
# }

# print(f"I am using {my_os["name"]} {my_os["version"]}.")

# for distro in distros:
#     print(distro.upper())

status =200

if status == 200:
    print("Success!")
elif status==404:
    print("Not Found!")
else:
    print("Unknown Error!")


numbers=[1,2,3,4,5]
squares=[]

# Traditional loop
for n in numbers:
    if n%2==0:
        squares.append(n*n)

print(squares)

# Loop using Comprehension, Python optimizes these to run faster than a standard 'for' loop
# Formula [expression for item in iterable if condition]
squares= [n*n for n in numbers if n%2!=0]
print(squares)

print('------------------------------------------')

users = ["alice", "vijay", "bob", "charlie"]
users_length= {name: len(name) for name in users }
print(
    users
)
print(users_length)
users_v= {name: name.endswith("y") for name in users}
print(users_v)

print('---------------------------------------------------')


servers = [
    {"name": "web-01", "status": "active"},
    {"name": "db-01", "status": "maintenance"},
    {"name": "cache-01", "status": "active"},
    {"name": "auth-01", "status": "offline"},
]

# CHALLENGE: Create a list of names for active servers only
active_servers=[s["name"].upper() for s in servers if s["status"]=="active"]
print(f"Active Servers: {active_servers}")

trouble_servers={s["name"]: s["status"] for s in servers if s["status"]!="active"}
print(f"Check these: {trouble_servers}")
