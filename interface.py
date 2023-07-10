import tkinter
from tkinter import *
import PIL
from PIL import ImageTk,Image
import maincode, matrix1, matrix2, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7

app = Tk()
app.title("Block Unblock")
image2 =Image.open('blocks.jpg')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
app.geometry('%dx%d+0+0' % (w,h))

labelText = StringVar()
labelText.set("Block Unblock")

label1 = Label(app, image=image1)
label1.place(x=0, y=0, relwidth=1, relheight=1)

#Create a canvas
my_canvas= Canvas(app, width=800, height=500)
my_canvas.pack(fill="both", expand=True)

#set image in canvas
my_canvas.create_image(0,0, image=image1, anchor="nw")

playb=Button(app, text="Play", command=maincode.maincode, padx=50, pady=10)

def instructions():
    im1 = PIL.Image.open(r"instructions.png")
    im1.show()
def credit():
    im2 = PIL.Image.open(r"credits.jpg")
    im2.show()

instb=Button(app, text="Instructions", command=instructions, padx=32,pady=10)
credb=Button(app, text="Credits", command=credit, padx=45,pady=10)

playb = my_canvas.create_window(10, 10, anchor="nw", window=playb)
instb = my_canvas.create_window(150, 10, anchor="nw", window=instb)
credb = my_canvas.create_window(295, 10, anchor="nw", window=credb)

app.mainloop()
