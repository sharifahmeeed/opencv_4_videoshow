import cv2
import numpy as np

img = cv2.imread("lena.jpg")

layer = img.copy()

gp = [layer] #gaussian pyramid array

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
   # cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended) 
    cv2.imshow(str(i), laplacian)

cv2.imshow("Orginal image", img)


cv2.waitKey()
cv2.destroyAllWindows()