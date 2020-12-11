import shapely, geopandas, fiona
import seaborn as sns
from fiona.crs import from_epsg,from_string
import pandas as pd
import matplotlib.pyplot as plt
import osmnx as ox

# place = 'D:/Program Files (x86)/pycharmProject/gaochun.osm'

# 显示道路信息
# place = '高淳区,南京市,江苏省,中国'
# gaochun = ox.graph_from_address(place)
#
# ox.plot_graph(gaochun)

# 显示地图轮廓
# tpath = 'C:/Users/小天/Desktop/林shp 2000 (1)/高淳二调-刘杉shp/高淳shp/镇.shp'
# tpath1 = 'C:/Users/小天/Desktop/林shp 2000 (1)/高淳二调-刘杉shp/高淳shp/村.shp'
# tpath2 ='C:/Users/小天/Desktop/林shp 2000 (1)/高淳二调-刘杉shp/高淳shp/小班.shp'
# zhen = geopandas.read_file(tpath)
# cun = geopandas.read_file(tpath2)
# # plot中的参数column='MIAN_JI', cmap='OrRd
# cun.plot()
# zhen.plot()
# plt.show()
