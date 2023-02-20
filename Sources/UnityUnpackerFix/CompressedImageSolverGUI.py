import tkinter as tk
from tkinter import filedialog
import CompressedImageSolverV2
from PIL import Image
from PIL import ImageDraw
from PIL import ImageTk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.fileMenu = None
        self.menuBar = None
        self.spriteNamesListbox = None
        self.metadataFilePath = ''
        self.pngFilePath = ''
        self.spriteInfos = {}
        self.rawImage = None
        self.img = None  # Prevent image garbage collect
        self.spriteCanvas = None

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 标题栏
        self.menuBar = tk.Menu(self)
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Open Meta File", command=self.open_meta_file)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=root.quit)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        self.mainFrame = tk.Frame(self)

        self.spriteNamesListbox = tk.Listbox(self.mainFrame, height=12)
        self.spriteNamesListbox.grid(row=0, column=0)
        self.spriteNamesListbox.bind("<<ListboxSelect>>", self.on_select)

        self.spriteCanvas = tk.Canvas(self.mainFrame, width=256, height=256, bd=4)
        self.spriteCanvas.grid(row=0, column=1)

        self.mainFrame.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def open_meta_file(self):
        extensions = [("Unity Asset Metadata", ".meta")]
        self.metadataFilePath = filedialog.askopenfilename(filetypes=extensions)
        self.pngFilePath = '.'.join(self.metadataFilePath.split('.')[:-1])
        self.spriteInfos = CompressedImageSolverV2.open_meta_file(self.metadataFilePath)
        # Load Image File
        self.rawImage = Image.open(self.pngFilePath)
        # Load list
        self.spriteNamesListbox.delete(0, tk.END)
        sprite_names_list = list(self.spriteInfos.keys())
        sprite_names_list.sort()
        for spriteName in sprite_names_list:
            self.spriteNamesListbox.insert(tk.END, spriteName)

        # Load photo for test
        # self.img = img = ImageTk.PhotoImage(self.rawImage)
        # self.spriteCanvas.create_image(0, 0, anchor=tk.NW, image=img)
        # print(self.spriteCanvas)

    def on_select(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        print('You selected item %d: "%s"' % (index, value))
        # Load Image
        print(f'image data: {self.spriteInfos[value]}')
        sprite_info = self.spriteInfos[value]
        crop_box = (
            sprite_info['x'],
            512 - sprite_info['y'] - sprite_info['height'],
            sprite_info['x'] + sprite_info['width'],
            512 - sprite_info['y']
        )
        crop_image = self.rawImage.crop(crop_box)
        self.img = crop_image = ImageTk.PhotoImage(crop_image)
        self.spriteCanvas.create_image(
            0,
            0,
            anchor=tk.NW,
            image=crop_image
        )


root = tk.Tk()
root.wm_attributes("-topmost", 1)
app = Application(master=root)
root.config(menu=app.menuBar)

app.mainloop()
