import os
import tkinter as tk
from tkinter import filedialog
import pil

root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

input_filenames = filedialog.askopenfilenames()