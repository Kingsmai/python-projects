#########################################################Import#########################################################
import os
import array as ay
import numpy as np
import tkinter as tk
from tkinter import filedialog
#########################################################Import#########################################################

########################################################Function########################################################
def _Check(data):
    #
    VerCode = np.array([85,110,105,116,121])
    VerCode = ay.array('B',VerCode).tobytes()
    #
    if VerCode==data:
        return True
    else:
        return False
def _Conversion(file_path):
    #
    fr = open(file_path, "rb")
    #
    data=fr.read()
    #
    fr.close()
    #
    if _Check(data[8:13]) == True:
        #
        data=data[8:]
        #
        fw = open(file_path, "wb")
        fw.write(data)
        fw.close()
        #
        _name = os.path.basename(file_path)
        #
        print(_name +"  "+ "转换完成。")
    else:
        #
        _name = os.path.basename(file_path)
        #
        print(_name +"  "+"无需转换。")
    
########################################################Function########################################################

##########################################################Main##########################################################
#
root=tk.Tk()
root.withdraw()
root.wm_attributes('-topmost',1)

#
func = input("【1】选择文件 【2】选择文件夹：")

#
if func == "1":
    #选择文件
    input_dir=filedialog.askopenfilename()
    #
    if input_dir == '':
        os._exit(0)
    #
    _Conversion(input_dir)
    #
    print("文件转换任务完成。")
    #
    os._exit(0)

#
if func == "2":
    #选择文件夹
    input_dir=filedialog.askdirectory()
    #
    if input_dir == '':
        os._exit(0)
    #
    filename = os.listdir(input_dir)
    #
    for file_path in filename:
        #
        file_path=os.path.join(input_dir,file_path)
        #
        if os.path.isdir(file_path):
            print("文件夹略过。")
        elif os.path.isfile(file_path):
            _Conversion(file_path)
        else:
            print("未识别的文件类型，略过。")
    #
    print("批量转换任务完成。")
    #
    os._exit(0)

#
print("输入错误。")
##########################################################Main##########################################################