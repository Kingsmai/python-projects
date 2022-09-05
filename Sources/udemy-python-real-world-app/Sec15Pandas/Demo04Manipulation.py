import pandas
from pandas.core.frame import DataFrame
# 读取用';'隔开txt文件，用read_csv函数
# 这个txt文件没有header（第一行列头），所以要带个参数：header=None
# 默认的Character-separated value (CSV)文件使用','分割，这个是用';'分割，参数：sep=';'
df = DataFrame(pandas.read_csv("supermarkets-no-header.txt", header=None, sep=";"))

# 没有Header（列头），默认会使用整数，可以定义一个：
# 注意：列表长度（元素数量）必须和数据列的长度一样长，否则会报错
df.columns = ["ID", "Address", "City", "ZIP", "Country", "Name", "Employees"]

# 默认会给一个index，从0开始。
# 比如我们这文档有个ID值可以作为表格索引，就用set_index函数修改表格索引
# 默认会返回一个新的DataFrame实例，而不会修改旧的实列。
#   如果要直接更改旧的实例，参数：inplace=True
# 默认更改后，会把被选中作为索引的那一列丢掉（drop）
#   如果要保留该列，则参数：drop=False
df.set_index("ID", inplace=True, drop=False)

# 如果我需要获取index(2,4]，"ZIP"到"Name"列的数据
print(df.loc["2":"4", "ZIP":"Name"])

# 如果我们需要获取"ZIP"列所有值
print(df.loc[:, "ZIP"])
# 上述获取的值转换成列表
print(list(df.loc[:, "ZIP"]))

# 也可以通过索引访问行和列：
print(df.iloc[1:3, 1:3])
# 所以，访问该列的所有元素：
print(df.iloc[:, 1:3])
# 获取某一行，某几列数据
print(df.iloc[3, 1:3])

# 删除某一行
# 第二个参数：（0是行，1是列）
df.drop(3, 0, inplace=True)
# 删除某一列
df.drop("City", 1, inplace=True)

# 删除某几行（连续）数据
df.drop(df.index[0:3], 0, inplace=True)
# 删除某几列（连续）数据
df.drop(df.columns[0:3], 1, inplace=True)

# 获取所有的行
print(df.index)
# 获取所有的列
print(df.columns)

# 【常用】：获取当前数据表有多少行数据
print(len(df.index))

# 获取当前表格有多少行、多少列（返回一个tuple）
print(df.shape)

# 增加某一列的数据值（所有）
# 增加一个叫Continent的列
df["Continent"] = df.shape[0] * ["North America"]
# df.shape[0]是获取当前数据表有多少行
# 列表 * 整数 = 一串长度为整数的值

# 如果一个列的所有行都需要同一个值（此方法也用于修改）
df["Continent"] = "USA, North America"

# 添加一行数据（这个概念有点绕）
# 我们先重新读取CSV
df = DataFrame(pandas.read_csv("supermarkets.csv"))
# 上面我们学会了用数字组成的index，其实index可以是其他【唯一】的值，比如我们现在用Address
df.set_index("Address", inplace=True)
print(df)
# 需要“转置”数据 -- 和矩阵转置概念差不多，行变列、列变行
df_t = df.T
# 这就跟增加一列的概念一样了
print(df_t)
# 计算下一个ID
nextId = int(df["ID"].iat[-1]) + 1
# 添加数据
df_t["My Address"] = [nextId, "NEW YORK", "New York 10001", "USA", "Donald A Langer", 32]
# 再一次转置
df = df_t.T
print(df)