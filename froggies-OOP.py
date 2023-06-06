import tkinter as tk
from PIL import Image, ImageTk
import os
<<<<<<< HEAD

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
=======
PATH = os.path.join(os.path.dirname(__file__), 'Photos')                          #VAZHLYVO!!!  
def froggies():
    global current_image
    current_image = 0
    window = tk.Tk()
    froggies = os.listdir(PATH)
    froggie_images = []
    for i in froggies:
        frog = Image.open(os.path.join(PATH, i))
        frog = frog.resize(size = (700, 700))
        img = ImageTk.PhotoImage(frog)
        froggie_images.append(img)
    def previous():
        global current_image
        current_image = (current_image - 1) % len(froggie_images)
        image.config(image = froggie_images[current_image])
    def next():
        global current_image
        current_image = (current_image + 1) % len(froggie_images)
        image.config(image = froggie_images[current_image])
    image = tk.Label(image = froggie_images[0])
    image.pack()
    nextbutton = tk.Button(text = '---->', command = next)
    previousbutton = tk.Button(text = '<----', command = previous)
    previousbutton.pack(side = tk.LEFT)
    nextbutton.pack(side = tk.RIGHT)
    window.mainloop()

if __name__ == '__main__':
<<<<<<<< HEAD:froggies.py
    froggies()
========
    window = tk.Tk()
    gallery = Gallery(window)
    window.mainloop() 
>>>>>>>> 9e480cf5fcc0e4eb8feb4413a7cab0c691ccbc83:froggies-OOP.py
>>>>>>> 9e480cf5fcc0e4eb8feb4413a7cab0c691ccbc83
