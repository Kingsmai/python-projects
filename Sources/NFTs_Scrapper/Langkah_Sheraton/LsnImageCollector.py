import json
import requests
import os


images_dict = {}
failed_img = {}

with open('Data/Langkah-Sheraton.json', 'r') as jsonFile:
    jsonData = json.load(jsonFile)
    data = jsonData['data']
    for token in data:
        images_dict[token['image']] = token['rarity']

images_dict = {k: v for k, v in sorted(images_dict.items(), key=lambda item: item[1])}

with open('Data/Langkah-Sheraton-Images.json', 'w') as outputJsonFile:
    json.dump(images_dict, outputJsonFile, indent=4)

# with open('Data/Langkah-Sheraton-Failed.json', 'r') as failedJsonFile:
    # images_dict = json.load(failedJsonFile)
    
    
# Scrap all Images
RARITY = {
    'R1': 'Original',
    'R2': 'Limited',
    'R3': 'Rare',
    'R4': 'Ultra Rare'
}

for rarity in RARITY:
    if not os.path.exists(f'Output/LSN/{RARITY[rarity]}'):
        os.makedirs(f'Output/LSN/{RARITY[rarity]}')

total_ipfs = len(images_dict)

for idx, (ipfs, rarity) in enumerate(images_dict.items()):
    print(f'Processing #{idx + 1} out of {total_ipfs}: {ipfs}')
    img_hash = str(ipfs).split('/')[-2]

    response = requests.get(ipfs, stream=True)
    
    if not response.ok:
        failed_img[ipfs] = rarity
    else:
        with open(f'Output/LSN/{RARITY[f"R{rarity}"]}/{img_hash}.jpg', 'wb') as handle:
            handle.write(response.content)

print("Operation done with these failed:")
for i in failed_img:
    print(i)

with open('Data/Langkah-Sheraton-Failed.json', 'w') as outputJsonFile:
    json.dump(failed_img, outputJsonFile, indent=4)