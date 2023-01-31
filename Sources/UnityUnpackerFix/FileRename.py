import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

input_filenames = filedialog.askopenfilenames()

dir_name = '/'.join(input_filenames[0].split('/')[:-1])

for idx, filepath in enumerate(input_filenames):
    filename = f'firework_{"0" + str(idx + 1) if idx + 1 < 10 else idx + 1}.png'
    new_filepath = os.path.join(dir_name, filename)
    os.rename(filepath, new_filepath)