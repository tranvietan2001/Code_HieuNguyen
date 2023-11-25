# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     low_b = np.uint8([5,5,5])
#     high_b = np.uint8([0,0,0])
#     mask = cv2.inRange(frame, high_b, low_b)
#     contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)

#     //show mask
#     //show frame

# cap.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread('your_image.jpg')

# Chuyển ảnh sang ảnh xám
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Áp dụng Gaussian Blur để làm mờ ảnh
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Phát hiện cạnh trong ảnh
edges = cv2.Canny(blur, 50, 150)

# Dò line bằng phương pháp Hough Line Transform
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

# Vẽ các line lên ảnh gốc
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Hiển thị ảnh
cv2.imshow('Detected Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

