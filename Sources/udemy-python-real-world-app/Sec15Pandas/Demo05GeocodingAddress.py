from geopy import Nominatim, ArcGIS
import geopy
# 使用geopy需要联网，因为他需要将地址传递给互联网服务，并从在线数据库获取坐标信息并计算经纬度返回来
# from geopy.geocoders import Nominatim
# nom = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75")
from geopy.geocoders import ArcGIS
import pandas
agis = ArcGIS()
# n = agis.geocode("3995 23rd Street, San Francisco, CA 94114")
# print(type(n)) # <class 'geopy.location.Location'>
# print(n.latitude) # 37.75292200397371
# print(n.longitude) # -122.43169700840102

df = pandas.read_csv("supermarkets.csv")
# 创建新的一列，保存完整的地址信息（用于给geocode使用）
df["Addr"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]
# 使用apply函数，将addr的值传给geocode函数（所以不用像上面一样要传递参数了）
df["Coordinates"] = df["Addr"].apply(agis.geocode)
# lambda x: x.longitude if x != None else None
# 上面是个Lambda表达式，后面带上个条件判断是因为，如果geocoder没有查询到某个地址，则会返回None，但None是不会有long或lat属性的，所以要避开
# 理解上就是：如果 X 不等于 None，则读取 x 的坐标，否则赋值 None
df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df)

df.to_csv("Supermarkets-geocoded.csv")