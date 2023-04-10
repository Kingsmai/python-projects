def is_prime(number):
    # 小于等于1的数字都不是素数
    if number <= 1:
        return False

    # 循环判断是否有其他因子
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    # 如果没有其他因子，则是素数
    return True


input_number = int(input("请输入一个正整数："))

if is_prime(input_number):
    print("{}是素数".format(input_number))
else:
    print("{}不是素数".format(input_number))
