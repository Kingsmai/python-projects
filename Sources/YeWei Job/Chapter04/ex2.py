# 从键盘获取API值
api = int(input("请输入API值: "))

# 根据API值判断空气质量
if api <= 50:
    print("优")
elif api <= 99:
    print("良")
elif api <= 199:
    print("轻度污染")
elif api <= 299:
    print("中度污染")
else:
    print("重污染")
