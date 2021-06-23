from PIL import Image, ImageDraw, ImageFont
import colorsys as colors
import math
import os
import sys
nineup = '#'
ninedown = '$'
eightup = '8'
eightdown = '9'
sevenup = '5'
sevendown = '&'
sixup = '0'
sixdown = 'O'
fiveup = '%'
fivedown = '='
fourup = '*'
fourdown = '<'
threeup = '>'
threedown = '+'
twoup = '-'
twodown = '!'
oneup = ';'
onedown = ','
zeroup = '.'
zerodown = ' '


characters = {
    "1.0": nineup,
	"0.99": nineup,
	"0.98": nineup,
	"0.97": nineup,
	"0.96": nineup,
	"0.95": ninedown,
	"0.94": ninedown,
	"0.93": ninedown,
	"0.92": ninedown,
	"0.91": ninedown,
	"0.9": eightup,
	"0.89": eightup,
	"0.88": eightup,
	"0.87": eightup,
	"0.86": eightup,
	"0.85": eightdown,
	"0.84": eightdown,
	"0.83": eightdown,
	"0.82": eightdown,
	"0.81": eightdown,
	"0.8": sevenup,
	"0.79": sevenup,
	"0.78": sevenup,
	"0.77": sevenup,
	"0.76": sevenup,
	"0.75": sevendown,
	"0.74": sevendown,
	"0.73": sevendown,
	"0.72": sevendown,
	"0.71": sevendown,
	"0.7": sixup,
	"0.69": sixup,
	"0.68": sixup,
	"0.67": sixup,
	"0.66": sixup,
	"0.65": sixdown,
	"0.64": sixdown,
	"0.63": sixdown,
	"0.62": sixdown,
	"0.61": sixdown,
	"0.6": fiveup,
	"0.59": fiveup,
	"0.58": fiveup,
	"0.57": fiveup,
	"0.56": fiveup,
	"0.55": fivedown,
	"0.54": fivedown,
	"0.53": fivedown,
	"0.52": fivedown,
	"0.51": fivedown,
	"0.5": fourup,
	"0.49": fourup,
	"0.48": fourup,
	"0.47": fourup,
	"0.46": fourup,
	"0.45": fourdown,
	"0.44": fourdown,
	"0.43": fourdown,
	"0.42": fourdown,
	"0.41": fourdown,
	"0.4": threeup,
	"0.39": threeup,
	"0.38": threeup,
	"0.37": threeup,
	"0.36": threeup,
	"0.35": threedown,
	"0.34": threedown,
	"0.33": threedown,
	"0.32": threedown,
	"0.31": threedown,
	"0.3": twoup,
	"0.29": twoup,
	"0.28": twoup,
	"0.27": twoup,
	"0.26": twoup,
	"0.25": twodown,
	"0.24": twodown,
	"0.23": twodown,
	"0.22": twodown,
	"0.21": twodown,
	"0.2": oneup,
	"0.19": oneup,
	"0.18": oneup,
	"0.17": oneup,
	"0.16": oneup,
	"0.15": onedown,
	"0.14": onedown,
	"0.13": onedown,
	"0.12": onedown,
	"0.11": onedown,
	"0.1": zeroup,
	"0.09": zeroup,
	"0.08": zeroup,
	"0.07": zeroup,
	"0.06": zeroup,
	"0.05": zerodown,
	"0.04": zerodown,
	"0.03": zerodown,
	"0.02": zerodown,
	"0.01": zerodown,
    "0.0": zerodown
}

#Picture Initiation Functions
def GetImage(message, errormessage):
    path = input(message)
    if os.path.exists(path):
        return Image.open(path)
    else:
        ErrorResolve(message)
        
#Gets the Text File to Write to
def GetTextFile(message):
    path = input(message)
    if path[len(path) - 4:len(path)] != '.txt':
        path = path + ".txt"
        print(f"File didn't have .txt extension. Automatically added and reading: {path} . Press enter to continue.")
        input()
    return path

#Function for Processing Error
def ErrorResolve(message):
    print(message)
    input("Press 'Enter' to quit")
    quit()

#Writing Picture to Text file
def GetColorCloseness(red, green, blue):
    (hue, saturation, value) = colors.rgb_to_hsv(red / 255, green / 255, blue /255)
    characterindex = str((math.floor(value * 100) / 100))
    return characters[characterindex]

#Processes the image into text as well as writing it
def ProcessImage(x, y, img, f):
    finalmessage = ""
    for h in range(0, y, 1):
        for w in range(0, x, 1):
            try:
                r, g, b = img.getpixel((w, h))
                colortext = GetColorCloseness(r, g, b)
                finalmessage = finalmessage + colortext + colortext
            except:
                break
        finalmessage = finalmessage + "\n"
        if h % 10 == 0:
            sys.stdout.write(f"\r {h} rows done out of {y}!")
            sys.stdout.flush()
    f.write(finalmessage)
    f.close()

#Gets the required info for any picture and resizes it accordingly
def FrameProcessing(image, file, xreduction=2, yreduction=2):
    width, height = image.size
    resizedimage = image.resize((int(width / xreduction), int(height / yreduction)))
    ProcessImage(width, height, resizedimage, file)

#Function to Initialize Picture Conversion (Run this method to start it as it goes through all of the steps)
def GetInfo():
    defaultmessage = 'Path to File as well as extension type (.jpg, .png, etc) '
    errormsg = "File does't exist!"
    image = None
    try:
        image = GetImage(defaultmessage, errormsg)
    except:
        ErrorResolve('Error loading File. Filetype may not be supported or it could be a bug.')
    file = open(GetTextFile("Type the path where you want to put the file or just put the name if you want it in this folder "), 'w')
    FrameProcessing(image, file, 6, 6)


