from Tkinter import *
from PIL import ImageTk, Image
import sys
import random
root = None
maxSamples = 250

def createImage(imgFile):
    img = Image.open(imgFile)
    x,y = [random.randint(1333,2566), random.randint(1000,1900)]
    img = img.crop((x,y,x+100,y+100))
    return img

class MainWindow():

    def __init__(self, main):

        # canvas for image
        self.canvas = Canvas(main, width=200, height=200)
        self.canvas.grid(row=0, column=1)

        # images
        self.origImg = createImage(image)
        self.img = ImageTk.PhotoImage(self.origImg)

        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = NW, image = self.img)
        self.canvas.itemconfig(self.image_on_canvas,image=self.img)

        #button to change image
        self.button = Button(main, text="Class 1", command=self.onButtonYes, justify=RIGHT)
        self.button.grid(row=2, column=0)

        self.button = Button(main, text="Class 2", command=self.onButtonNo)
        self.button.grid(row=2, column=1)

        self.count = 0

        self.labelstring = "Press D for Class 1, Press F for Class 2\n " \
                           "Sections Classified: "

        self.label = Label(root,text=self.labelstring+str(self.count))
        self.label.grid(row=1, column=0, columnspan=2)

        main.bind('d', self.onButtonYes)
        main.bind('f', self.onButtonNo)
        main.bind('c', self.onButtonYes)
        main.bind('n', self.onButtonNo)

    def onButtonYes(self, _event=None):
        self.origImg.save(name+"/Yes/"+name+"_"+session+"_"+str(self.count)+"_yes.jpg");
        # next image
        self.origImg = createImage(image)
        self.img =  ImageTk.PhotoImage(self.origImg)

        # change image
        self.canvas.itemconfig(self.image_on_canvas, image = self.img)
        self.count = self.count + 1

        if(self.count > maxSamples):
            quit(self)

        self.label.config(text=self.labelstring+str(self.count))

    def onButtonNo(self, _event=None):
        self.origImg.save(name+"/No/"+name+"_"+session+"_"+str(self.count)+"_no.jpg");

        # next image
        self.origImg = createImage(image)
        self.img =  ImageTk.PhotoImage(self.origImg)

        # change image
        self.canvas.itemconfig(self.image_on_canvas, image = self.img)
        self.count = self.count + 1

        if(self.count > maxSamples):
            quit(self)


        self.label.config(text=self.labelstring+str(self.count))

    def quit(self):
        root.destroy()

image = sys.argv[1]
name = sys.argv[2]
session = sys.argv[3]

root = Tk()
root.title("Dataset Builder")
MainWindow(root)
root.mainloop()
