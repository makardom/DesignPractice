import numpy as np
import cv2

# reading image
image = cv2.imread("test2.jpg", cv2.IMREAD_UNCHANGED)

# convert image to grey
img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# take threshold image
ret, new_image = cv2.threshold(img_grey, 150, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(new_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# create an empty image for contours
img_contours = np.zeros(image.shape)
ret, img_contours = cv2.threshold(img_contours, -1, 255, 0)

cv2.drawContours(img_contours, contours, -1, (0, 0, 0))

cv2.imwrite("res2.jpg", img_contours)


# print(contours)

contours_array = []

for i in range(0, len(contours)):
    contour = []
    for j in range(0, len(contours[i])):
        point = [contours[i][j][0][0], contours[i][j][0][1]]
        contour.append(point)
    contours_array.append(contour)

for i in range(0, len(contours_array)):
    print("Contour #", i)
    print(contours_array[i])
# contours_array is final array of contours
