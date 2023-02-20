import tkinter as tk
from tkinter import filedialog
import CompressedImageSolverV2
from PIL import Image
from PIL import ImageDraw
from PIL import ImageTk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.sprite_infos = {}
        self.sprite_names_list = []
        self.current_sprite_index = 0
        self.current_sprite_name = tk.StringVar()

        self.main_frame: tk.Frame = None
        self.image_viewer: tk.Canvas = None
        self.next_btn: tk.Button = None
        self.below_btn: tk.Button = None
        self.new_line_btn: tk.Button = None
        self.slice_name: tk.Entry = None

        self.pack()
        # self.create_widgets()
        self.open_meta_file()

    def create_widgets(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack()
        self.image_viewer = tk.Canvas(self.main_frame, width=128, height=128)
        self.image_viewer.grid(row=0, column=0, rowspan=2)
        self.next_btn = tk.Button(self.main_frame, text="Next", command=self.next_slice)
        self.next_btn.grid(row=0, column=1)
        self.below_btn = tk.Button(self.main_frame, text="Below")
        self.below_btn.grid(row=1, column=1)
        self.slice_name = tk.Entry(self.main_frame, textvariable=self.current_sprite_name)
        self.slice_name.grid(row=2, column=0)
        self.new_line_btn = tk.Button(self.main_frame, text="New Line")
        self.new_line_btn.grid(row=2, column=1)
        pass

    def open_meta_file(self):
        extensions = [("Unity Asset Metadata", ".meta")]
        metadata_file_path = filedialog.askopenfilename(filetypes=extensions)
        png_file_path = '.'.join(metadata_file_path.split('.')[:-1])
        self.sprite_infos = CompressedImageSolverV2.open_meta_file(metadata_file_path)
        # Load Image File
        raw_image = Image.open(png_file_path)
        print(raw_image.info)
        print(raw_image.size)
        # Load list
        self.sprite_names_list = list(self.sprite_infos.keys())
        self.sprite_names_list.sort()
        # Load Image and Infos
        # self.current_sprite_name.set(self.sprite_names_list[self.current_sprite_index])

        for sprite_name in self.sprite_names_list:
            print(sprite_name)
            sprite_info = self.sprite_infos[sprite_name]
            print(sprite_info)
            crop_box = (
                sprite_info['x'],
                raw_image.size[0] - sprite_info['y'] - sprite_info['height'],
                sprite_info['x'] + sprite_info['width'],
                raw_image.size[1] - sprite_info['y']
            )
            crop_image = raw_image.crop(crop_box)
            # crop_image.show()
            print(crop_box)

    def next_slice(self):
        if self.current_sprite_index < len(self.sprite_names_list):
            self.current_sprite_index += 1
            self.current_sprite_name.set(self.sprite_names_list[self.current_sprite_index])
            print(self.current_sprite_index)


root = tk.Tk()
root.withdraw()
root.wm_attributes("-topmost", 1)
app = Application(master=root)

# app.mainloop()
