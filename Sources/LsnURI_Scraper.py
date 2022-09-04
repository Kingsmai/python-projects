import requests
import time

start_time = time.time()

with open("Data/Langkah-Sheraton.json", 'a') as file:
    file.writelines('{')
    for i in range(0, 8888):
        url = f"https://api.langkahsheraton.com/api/nft/ipfs/sheraton/metadata/box/{i}"
        response = requests.get(url)
        file.writelines(response.text + ',\n')
        if i % 100 == 0:
            print(f"Processing #{i}")
    file.writelines('}')

end_time = time.time()

print(f'Operation completed in {round(end_time - start_time, 2)} seconds.')