from PIL import Image
import colorsys as colors
print("The ASCII image generated is best looked at on a dark background.")
path = input("Path to File or Name of File if its in the same folder as well as extension type (.jpg, .png, etc) ")
try:
    image = Image.open(path)
except:
    print("Error loading picture! Make sure the path is right and if problems continue, move the picture into the same folder and just type the name and extension.")
    input("Press 'Enter' to quit")
    quit()
width, height = image.size
y = height
x = width
finalmessage = ""
pathtowrite = input("Type the path where you want to put the file or just put the name if you want it in this folder ")
if pathtowrite[len(pathtowrite) - 4:len(pathtowrite)] != '.txt':
    pathtowrite = pathtowrite + ".txt"
    print(pathtowrite)
    input()
f = open(pathtowrite, 'w')
def GetColorCloseness(red, green, blue):
    (hue, saturation, value) = colors.rgb_to_hsv(red / 255, green / 255, blue /255)
    pallete = (' ', '.', '-', '+', '*', '=', 'O', '0', '&', '#')
    return pallete[int(value*len(pallete))]
for h in range(y):
    for w in range(x):
        r, g, b = image.getpixel((w, h))
        colortext = GetColorCloseness(r, g, b)
        finalmessage = finalmessage + colortext + colortext
    finalmessage = finalmessage + "\n"
f.write(finalmessage)
f.close()


