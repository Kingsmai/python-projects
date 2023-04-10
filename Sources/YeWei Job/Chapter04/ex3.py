# 从键盘获取日期信息
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))

# 将1月和2月视为上一年的13月和14月
if month < 3:
    month += 12
    year -= 1

# 计算蔡勒公式中的各项值
century = year // 100  # 世纪数
year_of_century = year % 100  # 世纪的年数
w = (year_of_century + year_of_century // 4 + century // 4 - 2 * century + 26 * (month + 1) // 10 + day - 1) % 7

# 星期几对应的数字转化为中文输出
if w == 0:
    print("星期日")
elif w == 1:
    print("星期一")
elif w == 2:
    print("星期二")
elif w == 3:
    print("星期三")
elif w == 4:
    print("星期四")
elif w == 5:
    print("星期五")
else:
    print("星期六")
