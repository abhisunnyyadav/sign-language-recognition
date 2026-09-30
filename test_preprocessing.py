import cv2

img = cv2.imread("dataset/A/0.jpg")

print("Original Shape:", img.shape)

img = cv2.resize(img, (64, 64))

print("Resized Shape:", img.shape)

cv2.imshow("Resized Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()