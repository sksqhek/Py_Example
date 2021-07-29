import cv2 as cv

img = cv.imread("test.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_R = img.copy()
img_G = img.copy()
img_B = img.copy()
img_R[:,:,1] = 0
img_R[:,:,2] = 0
img_G[:,:,0] = 0
img_G[:,:,2] = 0
img_B[:,:,0] = 0
img_B[:,:,1] = 0

