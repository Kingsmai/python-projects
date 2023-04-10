def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


input_year = int(input("请输入一个年份："))
if is_leap_year(input_year):
    print(input_year, "是闰年")
else:
    print(input_year, "不是闰年")
