def zeller(year, month, date):
    # 判断月份是否为1或2月，如果是，则将月份调整为上一年的13或14月
    if month == 1 or month == 2:
        year = year - 1
        month = month + 12

    # Zeller公式中的常数项
    y = year % 100
    c = year // 100

    # 计算当天是星期几
    w = (c // 4 - 2 * c + y + y // 4 + 13 * (month + 1) // 5 + date - 1) % 7

    # 将星期几的编号转换为星期几的名称
    weekday_names = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
    weekday = weekday_names[w]

    return weekday


input_year = int(input("请输入年份："))
input_month = int(input("请输入月份："))
input_date = int(input("请输入日期："))

weekday = zeller(input_year, input_month, input_date)

print("{}年{}月{}日是{}".format(input_year, input_month, input_date, weekday))
