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


def prime_numbers(number):
    count = 0  # 计数器，用于记录每行输出的素数个数

    for i in range(2, number):
        if is_prime(i):
            print(i, end=' ')  # 输出素数
            count += 1

            # 如果已经输出了10个素数，就换行并将计数器归零
            if count == 10:
                print()
                count = 0

    # 如果最后一行不足10个素数，也要换行
    if count != 0:
        print()


number = int(input("请输入一个正整数："))
prime_numbers(number)