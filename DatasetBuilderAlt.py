from PIL import Image
import sys
import random
maxSamples = 250

def createImage(imgFile):
    img = Image.open(imgFile)
    x,y = [random.randint(1333,2566), random.randint(1000,1900)]
    img = img.crop((x,y,x+100,y+100))
    return img

image = sys.argv[1]
name = sys.argv[2]
session = sys.argv[3]

for i in xrange(1, maxSamples + 1):
    createImage(image).save(name+"/Maybe/"+name+"_"+session+"_"+str(i)+"_no.jpg");
