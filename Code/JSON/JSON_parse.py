import json


with open("task_json.json", "r") as file:
    data = json.load(file)

indent = 0
for i in data:
    for j in i:
        if j == "parameters":
            print("parameters:")
            for k in i[j]:
                print("\tname:", k["name"])
                print("\ttype:", k["type"])
            if not i[j]:
                print("\t", None)
        else:
            print(j + ":", i[j])
