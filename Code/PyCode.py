import cv2 as cv
import numpy as np

green_img = cv.imread('green3.jpg', cv.IMREAD_UNCHANGED)
full_img = cv.imread('full2.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(full_img, green_img, cv.TM_CCOEFF_NORMED)

#cv.imshow('Result', result)
#cv.waitKey()

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.8
if max_val >= threshold:
    print('Found needle.')
else:
    print('Needle not found.')
needle_w = green_img.shape[1]
needle_h = green_img.shape[0]
top_left = max_loc
bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
cv.rectangle(full_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

cv.imshow('Result', full_img)
cv.waitKey()
cv.imwrite('result.jpg', full_img)