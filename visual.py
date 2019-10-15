from tkinter import *
from PIL import Image   # import from Pillow
from PIL import ImageTk  # import from PIL lib


class Visualer:
    # def __init__():
        # self.address  # TODO

    def visualize(self, image_file):
        # create tkinter widget instance
        root = Tk()

        # bind canvas to root
        # TODO Changable screen size
        canvas = Canvas(root, height=1080, width=1920)
        canvas.pack()

        # TODO: make dir changable by the user
        # open image in tkinter format
        img = ImageTk.PhotoImage(Image.open(f'{image_file}'))

        canvas.create_image(0,0,anchor=NW,image=img)

        # keep window on display
        canvas.mainloop()

