'''
Requirements

# pip install opencv-python
# pip install numpy

'''

# Import necessary packages
import cv2
import numpy as np

# Reading image
img = cv2.imread(input('Enter the image path: '))

def cartoonize(img, k):

    # Convert the input image to gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Peform adaptive threshold
    edges  = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 8)

    # cv2.imshow('edges', edges)

    # Defining input data for clustering
    data = np.float32(img).reshape((-1, 3))

    print("shape of input data: ", img.shape)
    print('shape of resized data', data.shape)

    # Defining criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)

    # Applying cv2.kmeans function
    _, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    # print(center)

    # Reshape the output data to the size of input image
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    #cv2.imshow("result", result)

    # Smooth the result
    blurred = cv2.medianBlur(result, 3)

    # Combine the result and edges to get final cartoon effect
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)

    return cartoon


cartoonized = cartoonize(img, 8)

# Show the output

#cv2.imshow('input', img)
cv2.imwrite('cartoonized_img.jpg',cartoonized)
print("Image successfully converted to cartoonized Image.")

cv2.waitKey(0)
cv2.destroyAllWindows()