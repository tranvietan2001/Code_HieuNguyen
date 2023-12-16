import requests
import numpy as np
import cv2

ip = 'http://192.168.243.191/'

url = ip+'cam-hi.jpg'

url_data = ip+'data'

while True:
    
    l1 = 0
    l2 = 0
    l3 = 0
    r1 = 0
    r2 = 0
    r3 = 0
    data_control = ""

    response = requests.get(url)
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (640, 480))
    image_gray= cv2.imdecode(image_array,cv2.IMREAD_GRAYSCALE)

    threshold_value = 65  # Giá trị ngưỡng
    max_value = 255  # Giá trị tối đa sau cắt ngưỡng
    _, thresholded = cv2.threshold(image_gray, threshold_value, max_value, cv2.THRESH_BINARY_INV)
    thresholded = cv2.resize(thresholded, (640, 480))
    # cv2.imshow('Image', image)
    
        
    for i in range(0, 107):
        if thresholded[240,i] == 255:
            l1 = l1 + 1

    for i in range(107,215):
        if thresholded[240,i] == 255:
            l2 = l2 + 1
    
    for i in range(215,320):
        if thresholded[240,i] == 255:
            l3 = l3 + 1

    for i in range(320, 427):
        if thresholded[240,i] == 255:
            r1 = r1 + 1

    for i in range(427, 535):
        if thresholded[240,i] == 255:
            r2 = r2 + 1
    
    for i in range(535, 640):
        if thresholded[240,i] == 255:
            r3 = r3 + 1

    print("===========================")
    print("Left 1", l1)
    print("Left 2", l2)
    print("Left 3", l3)
    print("Right 1", r1)
    print("Right 2", r2)
    print("Right 3", r3)
    print("===========================")

    if l1== 0 and l2 <=10 and r2 <=5 and r3 == 0 and l3 >=85 and r1 >= 85:
        print("====> FORWARD")
        data_control = "F"
    elif l1== 0 and l2== 0 and r3 == 0 and r1 >=95 and l3 < 90 and r2 <= 108:
        print("====> RIGHT_1")
        data_control = "R1"
    elif l1==0 and l2==0 and l3==0 and(r1 >= 90 or r2 >= 90 or r3 >= 90):
        print("====> RIGHT_2")
        data_control = "R2"
    elif  l1==0 and l2==0 and l3==0 and r1 ==0 and r2 == 0 and r3 < 90:
        print("====> RIGHT_3")
        data_control = "R3"
    elif l1 == 0 and r2 == 0 and r3 == 0 and l3 == 105 and l2 <= 90 and r1 <=90:
        print("====> LEFT_1")
        data_control = "L1"
    elif r1==0 and r2==0 and r3==0 and(l1 >= 90 or l2 >= 90 or l3 >=90):
        print("====> LEFT_2")
        data_control = "L2"
    elif r1==0 and r2==0 and r3==0 and l2 ==0 and l3 == 0 and l1 <90:
        print("====> LEFT_3")
        data_control = "L3"
    else:
        print("====> STOP")
        data_control = "S"


    payload = {'payload': data_control}
    response = requests.post(url_data, data=payload)
    if response.status_code == 200:
        print('Yêu cầu POST thành công')
    else:
        print('Yêu cầu POST không thành công')



    cv2.circle(thresholded, (400,240), 5, (0, 255, 255),-1)
    cv2.circle(thresholded, (240,240), 5, (0, 255, 255),-1)
    cv2.imshow("image show mask", thresholded)
    cv2.imshow("image show", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()