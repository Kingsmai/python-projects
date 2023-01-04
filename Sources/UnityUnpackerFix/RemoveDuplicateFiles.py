import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

input_dir = filedialog.askdirectory()

if input_dir == '':
    exit(0)

print("Please input extensions: ")
ext = input("> ")

filenames = os.listdir(input_dir)

for filename in filenames:
    if '#' in filename:
        if filename[filename.index('#') + 1 : -(len(ext) + 1)].isdigit():
            print(filename)
            os.remove(os.path.join(input_dir, filename))