# 某公司计划建立两个药品配送点向 10 个药品连锁店送货，各药品连锁店的地址坐标和每日需求量如表 3-6 所示，运价均为 1，试确定两个药品配送点的地址，使送货运输费用最低。
import math
import matplotlib.pyplot as plt

# xPosition, yPosition, demand, (transportFee excluded)
nodesList = [
    [70, 70, 8],
    [95, 50, 10],
    [80, 20, 6],
    [20, 60, 5],
    [40, 10, 7],
    [10, 50, 8],
    [40, 60, 12],
    [75, 90, 11],
    [10, 30, 11],
    [90, 40, 9]
]


# 精确重心法迭代计算
def calculate_position(node_data_list: list):
    data_list = []

    for idx, nodeData in enumerate(node_data_list):
        new_node = {
            "xPos": nodeData[0],
            "yPos": nodeData[1],
            "demandSupply": nodeData[2],
            "distanceWithPredict": 1
        }
        data_list.append(new_node)

    precision = 0.000001
    previous_transport_fee = float('inf')

    i = 0
    while True:
        x_sum_product = 0.0
        y_sum_product = 0.0
        total_supply_demand = 0.0
        total_transport_fee = 0.0
        for node in data_list:
            x_sum_product += node["xPos"] * node["demandSupply"] / node["distanceWithPredict"]
            y_sum_product += node["yPos"] * node["demandSupply"] / node["distanceWithPredict"]
            total_supply_demand += node["demandSupply"] / node["distanceWithPredict"]
        predict_x = x_sum_product / total_supply_demand
        predict_y = y_sum_product / total_supply_demand
        for node in data_list:
            node["distanceWithPredict"] = math.dist([node["xPos"], node["yPos"]], [predict_x, predict_y])
            total_transport_fee += node["demandSupply"] * node["distanceWithPredict"]
        # print(x_sum_product, y_sum_product, total_supply_demand)
        # print(group_a)
        # print(predict_x, predict_y, total_transport_fee)
        if previous_transport_fee - total_transport_fee < precision:
            break
        previous_transport_fee = total_transport_fee
        i += 1

    result = {
        # "predict_x": round(predict_x, 2),
        # "predict_y": round(predict_y, 2),
        "predict_x": predict_x,
        "predict_y": predict_y,
        "total_transport_fee": total_transport_fee
    }
    print(result)
    print(f"Total iterate {i} times.")
    return result


# 首先分成两组
halfLen = int(len(nodesList) / 2)
group_a = nodesList[:halfLen]
group_b = nodesList[halfLen:]

for i in range(3):
    predict_1 = calculate_position(group_a)
    predict_2 = calculate_position(group_b)

    group_a.clear()
    group_b.clear()

    # 计算到预测点的费用，并根据费用较少的重新分组
    for node in nodesList:
        predict_1_fee = math.dist([node[0], node[1]], [predict_1["predict_x"], predict_1["predict_y"]]) * node[2]
        predict_2_fee = math.dist([node[0], node[1]], [predict_2["predict_x"], predict_2["predict_y"]]) * node[2]
        if predict_1_fee < predict_2_fee:
            group_a.append(node)
        else:
            group_b.append(node)

print(group_a)
print(group_b)

# 创建坐标系
fig, ax = plt.subplots()

# 绘制节点位置
for i, node in enumerate(nodesList):
    ax.scatter(node[0], node[1])
    ax.annotate(str(i + 1), (node[0], node[1]))

# 绘制 group_a 和 group_b 位置
ax.scatter([x[0] for x in group_a], [x[1] for x in group_a], marker='s', color='r')
ax.scatter([x[0] for x in group_b], [x[1] for x in group_b], marker='s', color='b')

# 绘制 predict_1 和 predict_2 点
ax.scatter(predict_1['predict_x'], predict_1['predict_y'], marker='x', color='r')
ax.scatter(predict_2['predict_x'], predict_2['predict_y'], marker='x', color='b')

# 连接 predict_1 和 group_a
for point in group_a:
    ax.plot([predict_1['predict_x'], point[0]], [predict_1['predict_y'], point[1]], 'r--')

# 连接 predict_2 和 group_b
for point in group_b:
    ax.plot([predict_2['predict_x'], point[0]], [predict_2['predict_y'], point[1]], 'b--')

# 显示坐标系
plt.show()
