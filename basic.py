import cv2
import numpy as np

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce image noise and detail
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)

# Display the original image and the edges
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

