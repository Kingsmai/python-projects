import cv2
import numpy
# 读取图片，（0是灰阶，1是BGR）
im_g = cv2.imread("smallgray.png", 0)
print(im_g)
cv2.imwrite("newsmallgray.png", im_g)

# im_g 是个二维数组，获取第一维的前两个：
print(im_g[0:2])

# 获取第一维的前两个的第三第四个元素
print(im_g[0:2, 2:4])

# 例子：获取最后一个元素
print(im_g[2:4])

# 获取im_g的形状（多少行多少列）
print(im_g.shape)

# 迭代 numpy array 打印每一行
for row in im_g:
    print(row)

# 迭代 numpy array 打印每一列
for col in im_g.T:
    print(col)

# 迭代 numpy array 打印每一个元素
for pixel in im_g.flat:
    print(pixel)

# Stocking to numpy arrays
# hstack = horizontal stack
newImg = (
    (0, 10, 20, 30, 40, 50, 60, 70, 80, 90),
    (100, 110, 120, 130, 140, 150, 160, 170, 180, 190),
    (200, 210, 220, 230, 240, 250, 251, 253, 254, 255),
)
ims = numpy.hstack(newImg)
print(ims)

# 如果需要结合两个 numpy array，前提是两个数组的列数必须一样：
ims = numpy.hstack((newImg, im_g))
print(ims)
cv2.imwrite("combinedgreyh.png", ims)

newImg = (
    (0, 10, 20, 30, 40),
    (50, 60, 70, 80, 90),
    (100, 110, 120, 130, 140),
    (150, 160, 170, 180, 190),
    (200, 210, 220, 230, 240),
    (250, 251, 253, 254, 255),
)
ims = numpy.vstack((newImg, im_g))
print(ims)
cv2.imwrite("combinedgreyv.png", ims)

# 分割 numpy array，参数必须是要分割数组列的因素
# hsplit 最后的结果是：一列变成一行数组
lst = numpy.hsplit(ims, 5)
print(lst)

lst = numpy.vsplit(ims, 3) # 有9行，所以可以被3整除
print(lst)
# 结果就是：Python list 里包含 numpy array
