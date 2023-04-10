import math

xList = [70, 95, 80, 20, 40, 10, 40, 75, 10, 90]
yList = [70, 50, 20, 60, 10, 50, 60, 90, 30, 40]
supList = [8, 10, 6, 5, 7, 8, 12, 11, 11, 9]
transportFee = 1

shopNodes = []

# Convert into List Dictionary
for i in range(len(xList)):
    node = {
        "id": i + 1,
        "x": xList[i],
        "y": yList[i],
        "supply": supList[i],
        "transportFee": 1
    }
    shopNodes.append(node)

print(shopNodes)

halfLen = int(len(shopNodes) / 2)

# 初始解 =SUMPRODUCT(C2:C6,E2:E6,F2:F6)/SUMPRODUCT(E2:E6,F2:F6)
# 分成两组（初始对半分）
groupA = shopNodes[:halfLen]
groupB = shopNodes[halfLen:]
# 迭代 17 次，找到两个配送点的地址坐标
print(math.prod([sum(xList[:halfLen]), sum(supList[:halfLen]), 5]))
print(math.prod([sum(supList[:halfLen]), 1]))
x = math.prod([sum(xList[:halfLen]), sum(supList[:halfLen]), 1]) / math.prod([sum(supList[:halfLen]), 1])
y = math.prod([sum(yList[:halfLen]), sum(supList[:halfLen]), 1]) / math.prod([sum(supList[:halfLen]), 1])
print(x, y)
distanceList = []
for i in range(halfLen):
    distance = math.dist([xList[i], yList[i]], [x, y])
    distanceList.append(distance)
    print(distance)

a = [70, 70]
dem = 8
p = [74.34, 46.15]
distance = math.dist(a, p)
print(distance * dem)
