'''
Requirements

# pip install img2pdf
'''
# Importing necessary libraries
from fileinput import filename
import img2pdf
from PIL import Image
import os

# storing image path
img_path = input('Enter Image Path: ')

# storing pdf 
converted_pdf = "converted_img2pdf.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# creating pdf file
with open(converted_pdf, "wb") as file:
    file.write(pdf_bytes)
    file.close()

image.close()


# output
print("Successfully converted image to pdf file")
