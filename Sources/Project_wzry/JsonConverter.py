import json
import csv

# 读取 JSON 数据并将其转换为 Python 字典
with open('./Output/wzry_heroes_data.json', 'r', encoding='utf8') as json_file:
    data = json.load(json_file)

# 创建 CSV 文件并写入数据
with open('./Output/wzry_heroes_data.csv', 'w', encoding='utf8', newline='') as csv_file:
    # 创建字典写入器，并写入字段标题
    writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
    writer.writeheader()

    # 写入字典数据
    for hero in data:
        writer.writerow(hero)
