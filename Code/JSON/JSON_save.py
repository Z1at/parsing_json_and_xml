import json
import random


with open("task_json.json", "r") as file:
    data = json.load(file)

for i in data:
    del i["isRoot"]
    i["value"] = random.randint(100, 200)

for i in data:
    print(i)

with open("save_json.json", "w") as file:
    json.dump(data, file, indent=3)
