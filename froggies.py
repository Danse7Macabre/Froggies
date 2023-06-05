import tkinter as tk
from PIL import Image, ImageTk
import os

PATH = os.path.join(os.path.dirname(__file__), 'Photos')           #VAZHLYVO!!!  


class Gallery:
    def __init__(self, root):
        self.current_image = 0
        self.froggies = os.listdir(PATH)
        self.froggie_images = []
        for i in self.froggies:
            frog = Image.open(os.path.join(PATH, i))
            frog = frog.resize(size = (700, 700))
            img = ImageTk.PhotoImage(frog)
            self.froggie_images.append(img)        
        self.image = tk.Label(root, image = self.froggie_images[0])
        self.nextbutton = tk.Button(root, text = '---->', command = self.next)
        self.previousbutton = tk.Button(root, text = '<----', command = self.previous)
        self.image.pack()
        self.previousbutton.pack(side = tk.LEFT)
        self.nextbutton.pack(side = tk.RIGHT)

    def previous(self):
        self.current_image = (self.current_image - 1) % len(self.froggie_images)
        self.image.config(image = self.froggie_images[self.current_image])
        
    def next(self):
        self.current_image = (self.current_image + 1) % len(self.froggie_images)
        self.image.config(image = self.froggie_images[self.current_image])


if __name__ == '__main__':
    window = tk.Tk()
    gallery = Gallery(window)
    window.mainloop() 