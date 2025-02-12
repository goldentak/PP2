import json

with open("json/sample-data.json", "r") as file:
    data = json.load(file)

#header
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)

#output(table)
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    desc = attributes["descr"] if attributes["descr"] else " "
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:<50} {desc:<20} {speed:<10} {mtu:<10}")
