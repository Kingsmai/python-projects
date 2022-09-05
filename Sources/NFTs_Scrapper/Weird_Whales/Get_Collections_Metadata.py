import json
import requests

QTY = 3350
# URL = "https://ipfs.io/ipfs/QmahofbWXSFHyWNrYdgDuaLS9CQHEHf3yYjjkmrHBVdjmK/{}"
URL = "https://cloudflare-ipfs.com/ipfs/QmahofbWXSFHyWNrYdgDuaLS9CQHEHf3yYjjkmrHBVdjmK/{}"
metadata = []
failed_metadata = []

with open('Data/Weird-Whales.json', 'w') as jsonOutput:
    jsonOutput.write('{[')
    for i in range(QTY):
        metadataUrl = URL.format(i)
        response = requests.get(metadataUrl)
        print('Processing #%s / %s: %s' % (i + 1, QTY, metadataUrl))
        if response.ok:
            jsonOutput.write(response.text + ',\n')
        else:
            print('Failed: %s' % (metadataUrl))
            failed_metadata.append(i)
    jsonOutput.write(']}')


print('Operation done with these failed: %s' % (failed_metadata))
