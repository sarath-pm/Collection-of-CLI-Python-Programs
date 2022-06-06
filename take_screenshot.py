'''
Requirements

# pip install pyscreenshot

'''

# import necessary py modules
import pyscreenshot

# To capture full screen
image = pyscreenshot.grab()

# to capture custom part of the screen
# image = pyscreenshot.grab(bbox=(10, 10, 200, 200)) # (x1, x2, y1, y2) axis

# To display the captured screenshot
image.show()

# To save the screenshot
image.save("screenshot.png")
