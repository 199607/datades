import osmnx as ox
import geopandas
import matplotlib.pyplot as plt


# 道路信息
place = '高淳区,南京市,江苏省,中国'
# gaochun = ox.graph_from_place(place)
# ox.plot_graph(gaochun)

# # 绘制地图轮廓
gaochun = ox.geocode_to_gdf(place)
# gaochun.plot()
# plt.show()

highway = ox.geometries_from_place(place,{'highway':True})
print(type(highway))
# highway.plot()
# plt.show()
res = geopandas.overlay(gaochun,highway,how='union')
res.plot()
