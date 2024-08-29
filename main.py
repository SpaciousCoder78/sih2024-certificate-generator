#sih certificate generator
#developed by : Aryan Karamtoth of Department of Information Technology, KITS Warangal

#importing modules
# importing modules
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import textwrap

# read the csv file
persons = pd.read_csv('persons.csv')

# function to remove '@' part from email and keep only the roll number
def format_email(email):
    return email.split('@')[0]

# create a dictionary to keep track of duplicate names
name_counter = {}

# iterate over the rows in the dataframe
# iterate over the rows in the dataframe
for index, row in persons.iterrows(): # adjust this range according to the number of students in a row
        name_field = f"Student Full Name"
        email_field = f"Email (Domain Mail ID)"
        if pd.notna(row[name_field]) and pd.notna(row[email_field]):
            name = row[name_field]
            email = format_email(row[email_field])
            roll_number = email.upper()  # use the roll number from the email

            # format the text to be printed on the image
            text = f"This is to certify that {name}, Roll No. {roll_number}, successfully participated in the Internal Hackathon for Smart India Hackathon 2024 at KITSW held on 31/08/2024"

            # wrap the text into multiple lines if it's too long
            wrapper = textwrap.TextWrapper(width=80)  # adjust width as needed
            text_lines = wrapper.wrap(text=text)

            im = Image.open("sample.jpg")
            draw = ImageDraw.Draw(im)
            location = (223, 423)
            text_color = (0, 0, 0)
            selectFont = ImageFont.truetype("arial.ttf", size=25)

            # draw each line of text
            for line in text_lines:
                draw.text(location, line, fill=text_color, font=selectFont)
                location = (location[0], location[1] + 30)  # move location for next line

            # create a unique key using the name, email, and index
            unique_key = f"{name}_{email}_{index}"

            # append the counter to the file name
            im.save(f"certificates\\certificate_{unique_key}.jpg")