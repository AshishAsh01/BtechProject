from PIL import Image
import os
import glob

def imgcrop(input, xPieces, yPieces):
    filename, file_extension = os.path.splitext(input)
    im = Image.open(input)
    imgwidth, imgheight = im.size
    height = imgheight // yPieces
    width = imgwidth // xPieces
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
            try:
                a.save(filename + "-" + str(i) + "-" + str(j) + file_extension)
            except:
                pass
path = r"C:\Users\LENOVO\Desktop\Project images\CP 2D slices images\*.*"
for file in glob.glob(path):
    imgcrop(file, 4 , 1)
