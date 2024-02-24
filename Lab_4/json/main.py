import json

f_path ="Lab_4\json\data.json"
f = open(f_path)
x = json.load(f)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

for object in x["imdata"]:
    object1 = object["l1PhysIf"]["attributes"]
    print(f'{object1["dn"]}                               {object1["speed"]}   {object1["mtu"]}')