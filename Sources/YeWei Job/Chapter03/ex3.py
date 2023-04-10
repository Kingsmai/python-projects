import random

nums = []  # 创建一个空数组来存储生成的随机数
for i in range(3):
    nums.append(random.randint(1, 100))  # 随机生成一个100以内的自然数，并添加到数组中

sum_of_nums = sum(nums)  # 使用数组的加法操作计算数组中所有数的总和

print(f"The sum of {nums[0]}, {nums[1]}, and {nums[2]} is {sum_of_nums}.")  # 输出结果
