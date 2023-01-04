import tkinter as tk
from tkinter import Frame, ttk

VERSION = 'alpha 0.1'

class MainApplication(tk.Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__()
        ttk,Frame.__init__(self, master, *args, **kwargs)
        self.master = master

app = tk.Tk()
app.title(f"Fancy Editor v{VERSION}")
app.geometry('640x480')

master = ttk.Frame(app)
master.pack(fill=tk.BOTH)

inputEntry = ttk.Entry(master)
inputEntry.pack(fill=tk.X)

outputTv = tk.StringVar()

outputEntry = ttk.Entry(master, state='readonly', textvariable=outputTv)
outputEntry.pack(fill=tk.X)
outputTv.set("Hello, world!")

if __name__ == '__main__':
    app.mainloop()