import cv2

img = cv2.imread('pet.jpg')
original = 'Original Image'
cv2.namedWindow(original)
cv2.moveWindow(original, 150, 30)
cv2.imshow(original, img)

cv2.waitKey(10**3)

modified = cv2.blur(img, ksize=(5, 5))
blur = 'Blur image'
cv2.namedWindow(blur)
cv2.moveWindow(blur, 800, 30)
cv2.imshow(blur, modified)

cv2.waitKey(0)
