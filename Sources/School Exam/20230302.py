# info={1:'小明',2:'小黄',3:'小兰'}
# name1 = info.get(4,'小红')
# name2 = info.get(1)


# def print_info(name, age=18):
#     print(name, age, sep=',')
# print_info("小明")
# print_info(age=12, name='小红')

# x = 3; y = 4; z = 5
# print(x < y and y < z)
# print(x + y > z or x - y > 1)
# print(not (x!= y))
# print((x - y) == (y - z))

# print(bin(12))

# she = float(input())
# kai = she + 273.15
# print(kai)

# numdict = {
#     '0': '零',
#     '1': '一',
#     '2': '二',
#     '3': '三',
#     '4': '四',
#     '5': '五',
#     '6': '六',
#     '7': '七',
#     '8': '八',
#     '9': '九',
#     '.': '点'
# }
# num = input()
# for n in num:
#     print(numdict[n], end='')

# def ishuiwen(s):
#     ctr = len(s)
#     i = 0
#     count = 1
#     while i <= (ctr / 2):
#         if s[i] == s[ctr - i - 1]:
#             count = 1
#             i += 1
#         else:
#             count = 0
#             break
#
#     return count == 1
#
#
# print(ishuiwen('1234432'))
# print(ishuiwen('123454321'))

# file = open('文件路径', 'a')

# r = int(input())
# area = 3.14 * r * r
# print(area)

i = 100
while i >= 0:
    if i % 2 == 0:
        print(i)
    i -= 1
