import requests
response = requests.get('http://www.ce.cn/xwzx/shgj/gdxw/index.shtml')
response.encoding = "gb2312"
print(response.text)