import numpy
n = numpy.arange(27)
print(n, type(n))
# n 是 numpy.ndarray (N dimentional array)

print(n.reshape(3, 9)) # 二维数组：3 * 9 = 27

n = numpy.arange(27)
print(n.reshape(3, 3, 3)) # 三维数组：3 * 3 * 3 = 27

# 用Python list创建一个Numpy数组
m = numpy.asarray_chkfinite([[123, 12, 123, 12, 33], [], []], dtype=object)
print(m, type(m))