import folium  # 将代码转换为HTML的库
import pandas
# 创建map对象，设置初始位置
location = [37, -119]
# 设置地图的风格
tiles = "Stamen Terrain"

# 创建一个Map世界地图对象
map = folium.Map(
    location=location,
    zoom_start=6,
    tiles=tiles
)

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])  # 获取所有的经度坐标
lon = list(data["LON"])  # 获取所有的维度坐标
elev = list(data["ELEV"])  # 获取高度
name = list(data["NAME"])  # 获取火山名
t = list(data["TYPE"])  # 获取火山名

# 气泡框名称
html = """
<b>Volcano name:</b> <a href="https://www.google.com/search?q=%%22{}%%22" target="_blank">{}</a><br>
<b>Height:</b> {}m<br>
<b>Volcanoes Type:</b> {}<br>
<b>Latitude:</b> {}<br>
<b>Longitude:</b> {}<br>
"""

fg = folium.FeatureGroup(name="My Map")


def color_producer(elevation):
    # 根据高度修改颜色
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 2000:
        return "orange"
    elif 2000 <= elevation < 3000:
        return "red"
    else:
        return "darkred"


# 用zip函数迭代两个数组
for lt, ln, el, name, t in zip(lat, lon, elev, name, t):
    coordinates = [lt, ln]
    # 弹出气泡
    iframe = folium.IFrame(
        html=html.format(
            name,
            name,
            el,
            t,
            lt,
            ln),
        width=250,
        height=100)
    popup = folium.Popup(iframe, parse_html=True)
    # fg.add_child(folium.Marker(location=coordinates, popup=popup, icon=folium.Icon(color=color_producer(el))))
    fg.add_child(
        folium.CircleMarker(
            location=coordinates,
            popup=popup,
            radius=6,
            fill_color=color_producer(el),
            color='grey',
            fill_opacity=0.7))

fg.add_child(
    folium.GeoJson(
        data=open(
            "world-min.json",
            "r",
            encoding="utf-8-sig").read(),
        style_function=lambda x: {  # x 是 world.json 里的 "features"
                'fillColor': 'green' if x["properties"]['POP2005'] < 10000000 
                else 'orange' if 10000000 <= x["properties"]['POP2005'] < 20000000
                else 'red'}))

map.add_child(fg)

map.save("Map1.html")
