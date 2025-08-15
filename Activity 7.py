import cv2

image = cv2.imread('example.jpg')

cv2.namedwindow('Loaded Image', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Loaded Image', 800,500)
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destoryAllWindows()
print(f"Image Dimension: {image.shape}")