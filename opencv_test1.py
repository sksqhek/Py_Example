
import cv2

import numpy as np

logo = cv2.imread('opencv_logo.png', cv2.IMREAD_COLOR)

background = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

ret, logo_mask = cv2.threshold(logo_gray, 240, 255, cv2.THRESH_BINARY)

logo_mask_inv = cv2.bitwise_not(logo_mask)

height, width = logo_gray.shape[:2]

background_cut = background[100:height+100, 200:width+200]#변경

img1 = cv2.bitwise_and(logo, logo, mask=logo_mask_inv)
cv2.imshow("logo", logo)
img2 = cv2.bitwise_and(background_cut, background_cut, mask=logo_mask)
cv2.imshow("background_cut", background_cut)
tmp = cv2.add(img1, img2)

background[100:height+100, 200:width+200] = tmp#변경

cv2.imshow("img", background)

cv2.waitKey(0)

