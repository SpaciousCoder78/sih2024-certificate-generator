#sih certificate generator
#developed by : Aryan Karamtoth of Department of Information Technology, KITS Warangal

#importing modules
# importing modules
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# read the csv file
persons = pd.read_csv('persons.csv')

# find all columns that contain "Student Full Name" in their name
name_columns = [col for col in persons.columns if "Student Full Name" in col]

# iterate over the name columns
for name_column in name_columns:
    # convert the column to a list
    namelist = persons[name_column].tolist()

    # iterate over the names in the list
    for i in namelist:
        im = Image.open("sample.jpg")
        draw = ImageDraw.Draw(im)
        location = (463, 513)
        text_color = (0, 0, 0)
        selectFont = ImageFont.truetype("arial.ttf", size=45)
        draw.text(location, i, fill = text_color, font = selectFont)
        im.save(f"certificates\\certificate_{i}.jpg")