import shapely, geopandas, fiona
import seaborn as sns
from fiona.crs import from_epsg,from_string
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

tpath = 'C:/Users/小天/Desktop/林shp 2000 (1)/高淳二调-刘杉shp/高淳shp/镇.shp'
# tpath = 'C:/Users/小天/Desktop/林shp 2000 (1)/高淳二调-刘杉shp/高淳shp/镇.shp'
# tpath = 'C:/Users/小天/Desktop/林shp 2000 (1)/高淳二调-刘杉shp/高淳shp/镇.shp'

shp_df = geopandas.GeoDataFrame.from_file(tpath, encoding='utf-8')
shp_df.head()  # 获取表头


# print(shp_df.head(20))