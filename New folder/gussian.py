import cv2

# Read the image
image = cv2.imread("OIP.jpg")

# Apply Gaussian blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imshow("Gaussian Blur", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
