import cmath

# 获取用户输入的系数
a, b, c = map(float, input("请输入一元二次方程的系数(a,b,c，以逗号分隔): ").split(','))

# 计算判别式
d = (b ** 2) - (4 * a * c)

# 计算根
if d >= 0:
    # 有两个不等实根或有两个相等实根
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    if x1 == x2:
        print("该方程有两个相等实根: x =", x1)
    else:
        print("该方程有两个不等实根: x1 =", x1, "x2 =", x2)
else:
    # 无实根
    print("该方程无实根")
