# manages the list of pics and modifies them if needed
import os
from PIL import Image

class PicManager:
    def __init__(self, filepath):
        '''
        Constructor
        '''
        self.FILE = filepath
        self.picList = []
    
    def getList(self):
        '''
        gets a list from the generated .txt file with the images
        '''
        file = open(self.FILE, "r")
        data = file.read()
        dataToList = data.splitlines()
        self.picList = dataToList[:] # gets rid of last empty space, change to gets rid of empty ""
        file.close()
        return self.picList

    def getPics(self, num):
        '''
        gets the imageFilePath of num pics and removes them from the list
        '''
        # check if it's empty!!!
        i = 0
        retList = []
        while i < num:
            retList.append(self.picList.pop(0))
            print(i)
            i += 1
        return retList

    def rewriteFile(self):
        '''
        rewrites the file and removes image paths that have already been posted
        '''
        file = open(self.FILE, "w")
        for pic in self.picList:
            file.write(pic)
            file.write('\n')
        file.close()
    
    def resizePics(self, dir):
        '''
        resizes ever pic in the directory provided to a square standard
        '''
        thumbSize = 1080

        for filename in os.scandir(dir):
            f = os.path.join(dir, filename)
            if filename.is_file():
                if filename.path[-3:] == "JPG":
                    tempPath = None
                    filename = filename.path
                    
                else:
                    tempPath = filename.path
                    filename = tempPath.split('.')[0] + ".JPG"
                    
                im = Image.open(f)
                im_thumb = self.expand2square(im, (255, 255, 255)).resize((thumbSize, thumbSize), Image.LANCZOS)
                im_thumb.save(filename, quality=95)
                # remove the file with different extension
                if tempPath != None:
                    os.remove(tempPath)

        # for filename in os.listdir(dir):
        #     f = os.path.join(dir, filename)
        #     # checking if it is a file
        #     if os.path.isfile(f):
        #         print(f.path)
        #         im = Image.open(f)
        #         im_thumb = self.expand2square(im, (255, 255, 255)).resize((thumbSize, thumbSize), Image.LANCZOS)
        #         #im_thumb.save(filename, quality=95)

    def expand2square(self, pil_img, background_color):
        '''
        add padding to pil image, from https://note.nkmk.me/en/python-pillow-square-circle-thumbnail/
        '''
        width, height = pil_img.size

        if width == height:
            return pil_img
        elif width > height:
            result = Image.new(pil_img.mode, (width, width), background_color)
            result.paste(pil_img, (0, (width - height) // 2))
            return result
        else:
            result = Image.new(pil_img.mode, (height, height), background_color)
            result.paste(pil_img, ((height - width) // 2, 0))
            return result
                