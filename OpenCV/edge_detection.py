import cv2

img = cv2.imread('pet.jpg')

original = 'Original Image'
cv2.namedWindow(original)
cv2.moveWindow(original, 150, 30)
cv2.imshow(original, img)

cv2.waitKey(10**3)

modified = cv2.Canny(img, 50, 150)
canny = 'Canny Image'
cv2.namedWindow(canny)
cv2.moveWindow(canny, 800, 30)
cv2.imshow(canny, modified)

cv2.waitKey(0)
