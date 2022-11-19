import requests

w=input("网站名称：")
kw = {'s':'python 教程'}

# 设置请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
try:
    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    response = requests.get(w,params = kw, headers = headers)

    # 查看完整url地址
    print (response.url)
    # 查看响应内容，response.text 返回的是Unicode格式的数据
    #print(response.text)
    a=int(input("是否更新？0 不/1 是"))
    if a==1:
        with open("website.txt", "w", encoding="utf-8") as file:
            file.write(response.text)
            print("已更新")
except requests.exceptions.MissingSchema:
    print("没有名为"+w+"的网站")
