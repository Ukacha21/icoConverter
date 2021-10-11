from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.geometry("480x480")
root.title(".ico Converter")
root.iconbitmap("icon.ico")

font = ("comic sans", 12)

imageLabel = Label(root, text=" ")

def ask():
    opened_fil = filedialog.askopenfilename(filetypes=[("JPEG photo files", "*.jpg"), ("PNG files", "*.png"), ("icon files", "*.ico")])

    opened_file = Image.open(opened_fil)

    imageLabel.config(text = opened_file)

    def convert():
        opened_file.save(filedialog.asksaveasfilename(filetypes=[("Icon files", "*.ico")]))

    convertButton = Button(root, text="Convert to .ico", command=convert)
    convertButton.pack()

    

ask_Button = Button(root, text="Browse Pic", font=font, command=ask)

imageLabel.pack()
ask_Button.pack()

mainloop()