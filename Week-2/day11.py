# Writing
#with open("memory.txt", "w") as f:
#     f.write("The secret passcode is 12345.")
#
# with open("memory.txt", "r") as f:
#     content = f.read()
#     print(content)

import json

data = { "agent_name": "Tux", "status": "active", "tasks": 5}

with open("data.json","w") as f:
    json.dump(data, f, indent=4)

with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data)