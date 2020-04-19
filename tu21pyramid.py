import cv2
import numpy as np

img = cv2.imread("lena.jpg")

lr1 = cv2.pyrDown(img) #reduce resulation
lr2 = cv2.pyrDown(lr1)
hr = cv2.pyrUp(lr2)
cv2.imshow("Orginal image", img)
cv2.imshow("Pyrdown 1 image", lr1)
cv2.imshow("Pyrdown 2 image", lr2)
cv2.imshow("Pyrup 2 image", hr)

cv2.waitKey()
cv2.destroyAllWindows()