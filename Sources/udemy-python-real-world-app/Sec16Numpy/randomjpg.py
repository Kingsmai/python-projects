import numpy, cv2, random

data = [random.randint(0,255) for _ in range(1171875)]
data = numpy.resize(data,(625,625,3))
print(data)
cv2.imwrite("1.jpg", data)
s = cv2.imread('1.jpg')
cv2.imshow('img1',s)
cv2.waitKey(0)