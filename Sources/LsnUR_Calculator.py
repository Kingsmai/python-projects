import json

ur_counter = 0

with open('Data/Langkah-Sheraton.json', 'r') as file:
    data = json.load(file)
    for i in data['data']:
        if i['rarity'] == 4:
            print(i['name'])
            ur_counter += 1

print('Total have', ur_counter, 'Ultra Rares')