import csv
import re
import requests
import pandas as pd


def PrintList(ll):
    for item in ll:
        print(item)


result = []
response = requests.get(f'http://www.ce.cn/xwzx/shgj/gdxw/index.shtml')
response.encoding = "gb2312"
html = response.text
pattern = '&middot;<a\shref="(.+?)">([\d\D]+?)</a>.+?f2">(.+?)\s'
result += re.findall(pattern, html)
# PrintList(result)
for i in range(1, 10):
    response = requests.get(f'http://www.ce.cn/xwzx/shgj/gdxw/index_{i}.shtml')
    response.encoding = "gb2312"
    html = response.text
    pattern = '&middot;<a\shref="(.+?)">([\d\D]+?)</a>.+?f2">(.+?)\s'
    result += re.findall(pattern, html)
PrintList(result)
print(len(result))

# 导入python中的内置模块csv
with open("content.csv", "w") as f:
    w = csv.writer(f)
    w.writerows(result)

# 读取数据
pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
df = pd.read_csv("content.csv", names=["path", "title", "date"])
print(df.head())

# 根据日期进行分组并取数量最多的前10天
df1 = df.groupby("date").count()["title"].sort_values().tail(10)
# 查看每天的新闻数量
print(df1)

import matplotlib.pyplot as plt


# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['figure.figsize'] = (10, 5)  # 设置figure_size尺寸

# x轴坐标
x = df1.index
# y轴坐标
y = df1.values
# 绘制柱状图
plt.bar(x, y)
# 设置x轴名称
plt.xlabel("日期",fontsize=14)
# 设置x轴名称
plt.ylabel("数量",fontsize=14)
plt.show()


# 开始作业
result = []
response = requests.get(f'http://www.ce.cn/xwzx/kj/index.shtml')
response.encoding = "gb2312"
html = response.text
pattern = '&middot;<a\shref="(.+?)">([\d\D]+?)</a>.+?f2">(.+?)\s'
result += re.findall(pattern, html)
# PrintList(result)
for i in range(1, 25):
    response = requests.get(f'http://www.ce.cn/xwzx/kj/index_{i}.shtml')
    response.encoding = "gb2312"
    html = response.text
    pattern = '&middot;<a\shref="(.+?)">([\d\D]+?)</a>.+?f2">(.+?)\s'
    result += re.findall(pattern, html)
PrintList(result)
print(len(result))

# 导入python中的内置模块csv
with open("content2.csv", "w") as f:
    w = csv.writer(f)
    w.writerows(result)

# 读取数据
pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
df = pd.read_csv("content2.csv", names=["path", "title", "date"])
print(df.head())

# 根据日期进行分组并取数量最多的前10天
df1 = df.groupby("date").count()["title"].sort_values().tail(10)
# 查看每天的新闻数量
print(df1)

import matplotlib.pyplot as plt


# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['figure.figsize'] = (10, 5)  # 设置figure_size尺寸

# x轴坐标
x = df1.index
# y轴坐标
y = df1.values
# 绘制柱状图
plt.bar(x, y)
# 设置x轴名称
plt.xlabel("日期",fontsize=14)
# 设置x轴名称
plt.ylabel("数量",fontsize=14)
plt.show()

# 拓展部分
titleList = ["macro/more/","xwzx/fazhi/","xwzx/shgj/gdxw/","xwzx/kj/"]
result = []
for item in titleList:
    response = requests.get(f'http://www.ce.cn/{item}index.shtml')
    response.encoding = "gb2312"
    html = response.text
    pattern = '&middot;<a\shref="(.+?)">([\d\D]+?)</a>.+?f2">(.+?)\s'
    result += re.findall(pattern, html)
    # PrintList(result)
    for i in range(1, 25):
        response = requests.get(f'http://www.ce.cn/{item}index_{i}.shtml')
        response.encoding = "gb2312"
        html = response.text
        pattern = '&middot;<a\shref="(.+?)">([\d\D]+?)</a>.+?f2">(.+?)\s'
        result += re.findall(pattern, html)

# 导入python中的内置模块csv
with open("content3.csv", "w") as f:
    w = csv.writer(f)
    w.writerows(result)