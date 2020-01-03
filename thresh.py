import cv2
import numpy as np
import sys
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

try:
    img = cv2.imread('xy.jpg')
    img2 = cv2.imread('xx.jpg')
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.plot(hist2)
    plt.legend()
    plt.show()
   # cv2.imshow("THRESHOLD IMAGE", thresh1)
except Exception as e:
    print(e)


if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


"""
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)


cv2.imwrite("bin_threshold.jpg", thresh1)
cv2.imwrite("bin_inv_threshold.jpg", thresh2)
cv2.imwrite("set0_threshold.jpg", thresh3)
cv2.imwrite("set0_inv_threshold.jpg", thresh4)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

"""
