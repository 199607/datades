import shapely
import numpy as np
import pandas as pd
import xlrd

test_path = 'C:/Users\小天\Desktop/test.xlsx'
path = 'D:\datamining\数据\粮食数据\江苏.xlsx'
pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

data = pd.DataFrame(pd.read_excel(test_path))


# 处理数据表中重复的数值
# data.drop_duplicates()
# 删除数据表中重复的数值
# data.drop_duplicates()

#对空值数据进行填充
# data.fillna(0)
'''利用表中数据对表进行填充
data['属性名1']=data['属性名1'].fillna(loandata['属性名2']

'''
# 对空值数据进行删除
# data.dropna()

# 去除数据中空格的三种方式。第一种是去除数据两边的空格，第二种是单独去除左边的空格，第三种是单独去除右边的空格。
# data['term']=data['term'].map(str.strip)
# data['term']=data['term'].map(str.lstrip)
# data['term']=data['term'].map(str.rstrip)

# 大小写转换
# 大小写转换的方法也有三种可以选择，分别为全部转换为大写，全部转换为小写，和转换为首字母大写。
# data['term']=data['term'].map(str.upper)
# data['term']=data['term'].map(str.lower)
# data['term']=data['term'].map(str.title)

# 检查数据段是否为字符、字母、数字。值为T或F
# data['仓房外温'].apply(lambda x: x.isalpha())
# data['仓房外温'].apply(lambda x: x. isalnum ())
# print(data['企业代码'].apply(lambda x: x. isdigit ()))

# 对极端值进行处理
# 对数据长度进行判断，其中我们主要关注最大值(max)和最小值(min)情况。
# data.describe().astype(np.int64).T
# 使用仓房外温均值对异常值进行替换
# data.replace([100000,36],data['仓房外温'].mean())

# 对数据格式进行更改，例如将仓房外温改为整数
# loandata['仓房外温']=loandata['仓房外温'].astype(np.int64)
# 特别注意日期类型
# data['上传时间']=pd.to_datetime(data['上传时间'])
# 显示各个列的数据类型
# print(data.dtypes)

# 对数据进行分组********************************************在数据表的open_acc字段记录了贷款用户的账户数量，这里我们可以根据账户数量的多少对用户进行分级，5个账户以下为A级，5-10个账户为B级，依次类推
# bins = [0, 5, 10, 15, 20]
# group_names = ['A', 'B', 'C', 'D']
# loandata['categories'] = pd.cut(loandata['open_acc'], bins, labels=group_names)


# 对数组进行分列用test——path测试
grade_split = pd.DataFrame((x.split('|') for x in data.test),index= data.index,columns=['qian','hou'])
print( grade_split)

# 使用merge函数将数据匹配回原始数据表
data=pd.merge(data,grade_split,right_index=True, left_index=True)
print( data)

# print(data.dropna())