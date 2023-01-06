import os
import tkinter as tk
from tkinter import filedialog
import shutil

root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

# input_dir = filedialog.askdirectory()
input_dir = "C:/Users/xsbug/OneDrive/Desktop/sk4.3.8/Sprite_sorted"
output_dir = "C:/Users/xsbug/OneDrive/Desktop/sk4.3.8/Sprite_sorted/@standalone"

for root_dir, cur_dir, files in os.walk(input_dir):
    if len(files) == 1:
        current_file = os.path.join(root_dir, files[0])
        shutil.move(current_file, output_dir)
        os.rmdir(root_dir)