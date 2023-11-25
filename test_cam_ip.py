import requests
import numpy as np
import cv2

url = 'https://example.com/your_image.jpg'

response = requests.get(url)
image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
