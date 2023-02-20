import time
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageDraw
import yaml
import re
from pprint import pprint

# root = tk.Tk()
# root.withdraw()
# root.wm_attributes("-topmost", 1)

# extensions = [("Unity Asset Metadata", ".meta")]
# file_path = filedialog.askopenfilename(filetypes=extensions)
file_path = "C:/Source/FYP/Assets/Sprites/SK/sactx-0-512x512-Uncompressed-floor-5fbdd8c7.png.meta"
png_file_path = '.'.join(file_path.split('.')[:-1])
print(png_file_path)

startTime = time.time()

# =========================================================
# Read sprite slice information
# =========================================================
with open(file_path, 'r', encoding='utf-8') as file_stream:
    sprite_infos = yaml.safe_load(file_stream)
    sprite_infos = sprite_infos['TextureImporter']
    sprite_infos = sprite_infos['spriteSheet']
    sprite_infos = sprite_infos['sprites']
    image_info = {
        'width': 0,
        'height': 0,
        'categories': {}
    }
    temp_sizes = {}
    for sprite_info in sprite_infos:
        rect_info = sprite_info['rect']
        slice_info = {
            'name': sprite_info['name'],
            'x': rect_info['x'],
            'y': rect_info['y'],
            'width': rect_info['width'],
            'height': rect_info['height'],
        }
        categoryName = re.findall(r'[a-z_]+[^_0-9]?', slice_info['name'])[0]
        if categoryName not in image_info['categories'].keys():
            image_info['categories'][categoryName] = {
                'spriteInfo': [],
                'maxWidth': 0,
                'maxHeight': 0
            }
            temp_sizes[categoryName + 'Width'] = 0
            temp_sizes[categoryName + 'Height'] = 0
        image_info['categories'][categoryName]['spriteInfo'].append(slice_info)
        temp_sizes[categoryName + 'Width'] += rect_info['width']
        image_info['width'] = max(image_info['width'], temp_sizes[categoryName + 'Width'])
        temp_sizes[categoryName + 'Height'] = max(temp_sizes[categoryName + 'Height'], rect_info['height'])

categoriesKeys = list(image_info['categories'].keys())
categoriesKeys.sort()

for keys in categoriesKeys:
    image_info['height'] += temp_sizes[keys + 'Height']

print(temp_sizes)
print(image_info)

currentSpriteInfo = image_info['categories']['door']['spriteInfo'][0]
print(currentSpriteInfo)

# =========================================================
# Slice the sprite to new file
# =========================================================
img = Image.open(png_file_path)
# coordinates from upper left, Unity is from lower left
# lower to upper = imageHeight - positionY - sliceHeight
slice_box = (
    currentSpriteInfo['x'],
    512 - currentSpriteInfo['y'] - currentSpriteInfo['height'],
    currentSpriteInfo['x'] + currentSpriteInfo['width'],
    512 - currentSpriteInfo['y'],
)
print(slice_box)
slice_img = img.crop(slice_box)
# slide_indicator = ImageDraw.Draw(img)
# slide_indicator.rectangle(slice_box, outline='red')
# slice_img.show()


print(f'Operation done in: {time.time() - startTime}ms')
