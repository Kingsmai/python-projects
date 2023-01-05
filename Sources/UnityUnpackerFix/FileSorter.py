import os
import re
import tkinter as tk
from tkinter import filedialog
import shutil

# root = tk.Tk()
# root.withdraw()
# root.wm_attributes('-topmost', 1)

# input_dir = filedialog.askdirectory()
input_dir = "C:/Users/xsbug/OneDrive/Desktop/sk4.3.8/Sprite"
output_dir = os.path.dirname(input_dir) + '/' + os.path.basename(input_dir) + '_sorted'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

filenames = os.listdir(input_dir)

current_folder = ''
STANDALONE_FOLDER = '@standalone'

for filename in filenames:
    current_filename = filename.lower()
    if '_' in current_filename:
        if re.match(r'\d_\d', current_filename):
            foldername = 'gold_number'
        elif re.match(r'[0-9]{3} 8\+1', current_filename):
            foldername = '8+1'
        else:
            foldername = current_filename.split('_')[0]
    elif re.match(r'[a-zA-Z\u4e00-\u9fff]+[0-9]\D', current_filename):
        foldername = re.split('\d+', current_filename)[0]
    elif re.match(r'[a-zA-Z\u4e00-\u9fff]+[0-9]{2}\D', current_filename):
        foldername = re.split('\d+', current_filename)[0] + '2'
    elif re.match(r'[a-zA-Z\u4e00-\u9fff]+[0-9]{3}\D', current_filename):
        foldername = re.split('\d+', current_filename)[0] + '3'
    elif re.match(r'[a-zA-Z\u4e00-\u9fff]+[0-9]{4}\D', current_filename):
        foldername = re.split('\d+', current_filename)[0] + '4'
    elif re.match(r'\d+', current_filename):
        foldername = STANDALONE_FOLDER
    else:
        foldername = STANDALONE_FOLDER
    
    current_filepath = os.path.join(input_dir, filename)
    target_dir = os.path.join(output_dir, foldername)
    target_filepath = os.path.join(target_dir, filename)
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    shutil.copy(current_filepath, target_filepath)
    # if False:
    #     continue
    # elif re.match("[a-zA-Z]+_[a-zA-Z]+\D", current_filename):
    #     print(current_filename)
    #     continue
    # elif '_' in current_filename:
    #     continue
    # elif re.match("[a-zA-Z]{1,20}[0-9]{1,20}", current_filename):
    #     continue
    # if foldername != current_folder:
    #     print(current_folder, foldername)
    #     current_folder = foldername