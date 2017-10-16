from PIL import Image
import os
from shutil import copyfile

def main():
    path = "./static/image"
    output_path = "./static/images"
    print("Compressing image without loosing quality")
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    basewidth = 960

    for file in files:
        if ".jpg" in file or ".JPG" in file or ".png" in file or ".jpeg" in file:
            print "- Converting:", file
            img = Image.open(os.path.join(path, file))
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)

            file = file.replace(".JPG", ".jpg")
            file = file.replace(".png", ".jpg")
            file = file.replace(".jpeg", ".jpg")
            img.save(os.path.join(output_path, file), optimize=True, quality=95)
        else:
            print "- Copying:", file
            copyfile(os.path.join(path, file), os.path.join(output_path, file))
if __name__ == '__main__':
    main()

from PIL import Image

# basewidth = 300
# img = Image.open('somepic.jpg')
# wpercent = (basewidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((basewidth,hsize), Image.ANTIALIAS)
# img.save('sompic.jpg')
