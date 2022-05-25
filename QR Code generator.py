'''
Requirements

# pip install pyqrcode
# pip install pypng

'''

# Python Modules
import pyqrcode 
import png 

# Input the details for the QR code.
qr = input("Enter the details to generate the QR code \n")

# Logic to create QR code.
url = pyqrcode.create(qr)
url.png("qr.png",scale=10)
