dividend = float(input("Please enter the dividend: "))  # 读取被除数
divisor = float(input("Please enter the divisor: "))  # 读取除数

if divisor == 0:  # 判断除数是否为零
    print("Error: divisor cannot be zero.")
else:
    quotient = dividend / divisor  # 计算商
    rounded_quotient = round(quotient, 2)  # 保留两位小数
    print(f"{dividend} {chr(10135)} {divisor} = {rounded_quotient}")