import tkinter as tk
from PIL import Image, ImageTk
import os
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
    froggies()