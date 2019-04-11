import cv2 as cv

src = cv.imread("./ls.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
print(help(cv.namedWindow))
cv.imshow("input image",src)
cv.waitKey(0)