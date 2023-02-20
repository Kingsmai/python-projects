import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.withdraw()
root.wm_attributes("-topmost", 1)

extensions = [("Images", ".jpeg .jpg .png .bmp .gif .ppm .tiff")]

file_path = filedialog.askopenfilename(filetypes=extensions)

img = Image.open(file_path, mode='r')
print(file_path)
print(img)
print("Image width: %s; height: %s" % (img.width, img.height))
width, height = img.size
print("Image size:", img.size)
print("Image format:", img.format)
print("Image is", ("readonly" if img.readonly else "read write"))
print("Image info:", img.info)
print("Image mode:", img.mode)

all_pixels = set()

# Process every pixel
for x in range(width):
    for y in range(height):
        current_color = img.getpixel((x, y))
        ####################################################################
        # Do your logic here and create a new (R,G,B) tuple called new_color
        if current_color[3] == 0:
            new_color = (0, 0, 0, 0)
        else:
            new_color = current_color
            all_pixels.add(current_color)
        ####################################################################
        img.putpixel((x, y), new_color)

# print(all_pixels)

# Generate color palette
color_palette = Image.new("RGBA", (1, len(all_pixels)))
print("Color Palette size:", color_palette.size)
for y, pixel in enumerate(all_pixels):
    color_palette.putpixel((0, y), pixel)

# pixels = list(img.getdata())
# pixels = [pixels[i * width: (i + 1) * width] for i in range(height)]
#
# pprint(pixels)

####################################################################
# Save
####################################################################

# mod_image_filepath = '/'.join(file_path.split('/')[:-1]) + '/' + file_path.split('/')[-1].split('.')[0] + ".mod.png"
# print(mod_image_filepath)
# img.save(mod_image_filepath)

# Save color palette
# color_palette_filepath = \
#     '/'.join(file_path.split('/')[:-1]) + '/' + file_path.split('/')[-1].split('.')[0] + ".plt.png"
# print(color_palette_filepath)
# color_palette.save(color_palette_filepath)

img.save(file_path)
