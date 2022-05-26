'''
Requirements

# pip install opencv-python

'''

# Import python module
import cv2

# Get the input from the user
image = cv2.imread(input("Enter the image path: "))

# Image converted to gray 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("converted_gray.png", gray_image)

# Image converted to inverted
inverted_image = 255 - gray_image
cv2.imwrite("converted_inv.png", inverted_image)

# Image converted to blurred
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
cv2.imwrite("converted_blur.png", blurred)

# Image converted to inverted blurred
inverted_blurred = 255 - blurred
cv2.imwrite("converted_invblur.png", inverted_blurred)

# Image converted to Pencil Sketch
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imwrite("converted_sketch.png", pencil_sketch)

# Output
print("Image successfully converted")