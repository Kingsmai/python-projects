import os

operateFolder = [
    'Luke',
    'Saint11',
    'Saint11-cn',
    'Slynyrd'
]

for folder in operateFolder:
    for root, dirs, files in os.walk(rf'./Output/{folder}'):
        for fileName in files:
            fnSplit = fileName.split('.')
            os.rename(f'{root}/{fileName}', f'{root}/{fnSplit[0]}.{fnSplit[-1]}')