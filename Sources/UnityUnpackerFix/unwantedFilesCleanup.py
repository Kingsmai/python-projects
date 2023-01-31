import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

input_dir = filedialog.askdirectory()

UNWANTED_EXT = [
    'anim',
    'meta',
    'prefab',
    'unity',
    'controller',
    'overrideController',
    'audioclip',
    'mixer',
    'lighting',
    'mat',
    'physicsMaterial2D',
    'renderTexture',
    'shader',
    'asmdef',
    'cs',
    'asset'
]

for root_dir, current_dir, files in os.walk(input_dir):
    for file in files:
        if file.split('.')[-1] in UNWANTED_EXT:
            os.remove(os.path.join(root_dir, file))
    if len(os.listdir(root_dir)) == 0:
        os.rmdir(root_dir)