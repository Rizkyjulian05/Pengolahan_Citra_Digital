#M.RIZKY JULIAN SAPUTRA
#NPM : 011190047
#KELOMPOK : OPERASI PENGENMBANAGAN (THRESHOLDING)
import cv2 as cv

gambar_123 = cv.imread('123.jpg')
cv.imshow('gambar 123 RGB',gambar_123)
gray_image = cv.cvtColor(gambar_123,cv.COLOR_RGB2GRAY)
cv.imshow('gambar 123 grayscale', gray_image)
_,binary_image = cv.threshold(gray_image,127, 255, cv.THRESH_BINARY)
cv.imshow('gambar 123 Binary', binary_image)
cv.waitKey(0)
cv.destroyAllWindows()