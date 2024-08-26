#sih certificate generator
#developed by : Aryan Karamtoth of Department of Information Technology, KITS Warangal

#importing modules
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# persons= pd.read_csv('persons.csv')

namelist = "name"
im=Image.open("sample.jpg")
draw = ImageDraw.Draw(im)
location = (100, 100)
text_color = (0, 188, 255)
selectFont = ImageFont.truetype("arial.ttf", size=45)
draw.text(location, namelist, fill = text_color, font = selectFont)
im.save("certificate.jpg")

