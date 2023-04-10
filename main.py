# 变量 income 接受 租金收入
# 变量 deductibleitems 接受 准予扣除项目
# 变量 cost 接收 修缮费用

# 财产租赁所得个税应纳税所得额计算为:
# 每次收入不超过 4000 元
# 应纳税所得额=每次收入额-准予扣除项目-修缮费用 (800元为限) -800元
# 每次收入超过 4000元
# 应纳税所得额=(每次收入额-准予扣除项目-修缮费用 (800元为限))* (1-20%)

# 请编写财产租赁所得个税应纳税所得额计算的代码逻辑。
def func(income, deductibleitems, cost):
    ### 修改代码开始 ###
    if income <= 4000:
        taxable_income = income - deductibleitems - min(cost, 800) - 800
    else:
        taxable_income = (income - deductibleitems - min(cost, 800)) * 0.8
    return taxable_income
