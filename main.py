#sih certificate generator
#developed by : Aryan Karamtoth of Department of Information Technology, KITS Warangal

#importing modules
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import textwrap

# read the csv file
persons = pd.read_csv('persons.csv')

# function to remove '@' part from email and keep only the roll number
def format_email(email):
    return email.split('@')[0]

# iterate over the rows in the dataframe
for index, row in persons.iterrows():
    if pd.notna(row["Student Full Name"]) and pd.notna(row["Email (Domain Mail ID)"]):
        name = row["Student Full Name"]
        email = format_email(row["Email (Domain Mail ID)"])
        roll_number = email.upper()  # use the roll number from the email
        problem_title = row["Problem Statement Title"]
        problem_number = row["Problem Statement Number (Example: SIH1281)"]

        # format the text to be printed on the image
        text1 = f"This is to certify that {name}, Roll No. {roll_number}, successfully participated in the Internal Hackathon for Smart India Hackathon 2024 at KITSW held on 31/08/2024."
        text2 = f"Problem Statement: {problem_title} ({problem_number})"

        # wrap the text into multiple lines if it's too long
        wrapper = textwrap.TextWrapper(width=80)  # adjust width as needed
        text_lines1 = wrapper.wrap(text=text1)
        text_lines2 = wrapper.wrap(text=text2)

        # combine the two lists of lines
        text_lines = text_lines1 + text_lines2

        im = Image.open("sample.jpg")
        draw = ImageDraw.Draw(im)
        location = (223, 533)
        text_color = (0, 0, 0)
        selectFont = ImageFont.truetype("arial.ttf", size=25)

        # draw each line of text
        for line in text_lines:
            draw.text(location, line, fill=text_color, font=selectFont)
            location = (location[0], location[1] + 30)  # move location for next line

        # create a unique key using the name, email, and index
        unique_key = f"{name}_{email}_{index}"
        unique_key = unique_key.replace(" ", "_")  # replace spaces with underscores

        # append the counter to the file name
        im.save(f"certificates\\certificate_{unique_key}.jpg")