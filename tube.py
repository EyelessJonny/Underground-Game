import json
import random

name = []

while True:
    with open('stations.json', 'r') as f:
        stations_dict = json.load(f)

    zone = str(input("Pick a maximum zone?\n"))
    if zone == "1":
        for station in stations_dict:
            if 1 in station["zones"]:
                name.append(station["name"])
    elif zone == "2":
        for station in stations_dict:
            if 1 in station["zones"] or 2 in station["zones"]:
                name.append(station["name"])
    elif zone == "3":
        for station in stations_dict:
            if 1 in station["zones"] or 2 in station["zones"] or 3 in station["zones"]:
                name.append(station["name"])
    else:
        print("Sorry this is unsupported.")
        break

    print(random.choice(name))
    print(random.choice(name))
