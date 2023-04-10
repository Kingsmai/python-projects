# 从键盘获取圆的信息
x1, y1, r1 = map(float, input("请输入第一个圆的圆心坐标和半径（格式为 x1,y1,r1）：").split(","))
x2, y2, r2 = map(float, input("请输入第二个圆的圆心坐标和半径（格式为 x2,y2,r2）：").split(","))

# 计算两圆心之间的距离
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 判断两圆之间的关系
if distance < abs(r2 - r1):
    print("第一个圆内含于第二个圆")
elif distance == abs(r2 - r1):
    print("第一个圆与第二个圆内切")
elif distance < r1 + r2:
    if distance == abs(r2 + r1):
        print("第一个圆与第二个圆外切")
    elif distance < abs(r2 + r1):
        print("第一个圆与第二个圆相交")
    else:
        print("第一个圆与第二个圆相离")
else:
    print("第一个圆与第二个圆相离")
