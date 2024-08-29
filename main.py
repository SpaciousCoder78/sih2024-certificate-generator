#sih certificate generator
#developed by : Aryan Karamtoth of Department of Information Technology, KITS Warangal

#importing modules
# importing modules
# importing modules
# importing modules
# importing modules
# importing modules
# importing modules
# importing modules
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import textwrap

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
        location = (223, 423)
        text_color = (0, 0, 0)
        selectFont = ImageFont.truetype("OpenSans-Regular.ttf", size=25)  # use Open Sans Regular font

        # format the text to be printed on the image
        text = f"This is to certify that {i} successfully participated in the Internal Hackathon for Smart India Hackathon 2024 at KITSW held on 31/08/2024"

        # wrap the text into multiple lines if it's too long
        wrapper = textwrap.TextWrapper(width=80)  # decrease width to increase line breaks
        text_lines = wrapper.wrap(text=text)

        # draw each line of text
        for line in text_lines:
            draw.text(location, line, fill=text_color, font=selectFont)
            location = (location[0], location[1] + 35)  # increase vertical spacing between lines

        im.save(f"certificates\\certificate_{i}.jpg")