import cv2

image = cv2.imread('pet.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
color = cv2.bilateralFilter(image, 9, 250, 250)

cartoon = cv2.bitwise_and(color, color, mask=edges)
cartoon2 = cv2.stylization(image, sigma_s=150, sigma_r=0.25)

modified = 'Cartoon 1'
cv2.namedWindow(modified)
cv2.moveWindow(modified, 150, 30)
cv2.imshow(modified, cartoon)

cv2.waitKey(10**3)

modified2 = 'Cartoon 2'
cv2.namedWindow(modified2)
cv2.moveWindow(modified2, 800, 30)
cv2.imshow(modified2, cartoon2)

cv2.waitKey(0)
