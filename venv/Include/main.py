import shapely, geopandas, fiona
import seaborn as sns
from fiona.crs import from_epsg,from_string
import pandas as pd
import matplotlib.pyplot as plt

tpath = 'C:/Users/小天/Desktop/林shp 2000 (1)/高淳二调-刘杉shp/高淳shp/镇.shp'


#geopandas的read_file方法可以读取shape文件，转化为GeoSeries和GeoDataFrame数据类型。
world = geopandas.read_file(tpath)#geopandas.datasets.get_path('naturalearth_lowres')

# # 新增一列，每个国家的中心点
# world['centroid_column'] = world.centroid
# # 将新增列设置为几何列
# world = world.set_geometry('centroid_column')

world.plot(column='MIAN_JI', cmap='OrRd')
print(type(world))
plt.show()
