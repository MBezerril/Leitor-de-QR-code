import cv2
import numpy as np
import math

img = cv2.imread('UP_AND_DOWN.png')
# img = cv2.resize(img, (800,600))
qcd = cv2.QRCodeDetector()
retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)

print(int(points[0][0][0]))
print(decoded_info)
img_rects = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)
for s, p in zip(decoded_info, points):
    img_rects = cv2.putText(img_rects, s, p[0].astype(int),
                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
# img_rects = cv2.circle(img_rects, (int(points[0][3][0]),int(points[0][3][1])), 5, (255,0,0), 10)
for index, qr_found in enumerate(decoded_info):
    point0 = (int(points[index][0][0]), int(points[index][0][1]))
    point1 = (int(points[index][1][0]), int(points[index][1][1]))
    point2 = (int(points[index][2][0]), int(points[index][2][1]))
    point3 = (int(points[index][3][0]), int(points[index][3][1]))
    vert1 = np.linalg.norm(np.subtract(point0,point1))
    vert2 = np.linalg.norm(np.subtract(point2,point3))
    print(f"{qr_found} drone sobe") if vert1 < vert2 else print(f"{qr_found} drone Desce")
    img_rects = cv2.circle(img_rects, (int(points[0][3][0]),int(points[0][3][1])), 5, (255,0,0), 10)

# cv2.imwrite('data/dst/qrcode_opencv.jpg', img_rects)

cv2.imshow('Result', img_rects)
cv2.waitKey(10000)
