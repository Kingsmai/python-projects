# （1）假设某门面出租，在租赁合同中规定的首年租金为100000块，租金每年涨5%。
# 在控制台打印出10年时间，每一年租金会分别涨到多少钱？
# （2） 如果某打工人想租下了该店面，花费了30万进行装修，开始通过销售服装获取收入。
# 第一个月刨除房租、水电、人工开销，能有收入5000块。
# 生意越来越好做，假设能够勉强维持每月收入7%递增，那需要多久的辛勤劳动，就能收回成本？
# 本题中，所有金额保留两位小数。
rental = 100000.00
for i in range(10):
    print(f"第{i + 1}年：{rental:.2f}")
    rental += rental * 0.05

investment = 300000
total_earn = 5000
month_passed = 0
while True:
    if total_earn > investment:
        break
    total_earn += total_earn * 0.07
    month_passed += 1

print(f"需要{month_passed}个月")
