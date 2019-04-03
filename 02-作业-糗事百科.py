import re
import time

# 作业2: 爬取糗事百科文本页的所有段子,结果如 : xx说: xxxx
# https://www.qiushibaike.com/text/page/1/   # 1表示页码

# 正则表达式提示： 
#	# 获取一个评论
#   regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
#	# 获取名称
#   nameCom = re.compile('<h2>(.*?)</h2>', re.S)
#	# 获取内容
#	contentCom = re.compile('<span>(.*?)</span>', re.S)
import urllib.request
from http import cookiejar

def getData(url):
    cookies = cookiejar.CookieJar()
    # 创建cookie处理器
    cookie_handler = urllib.request.HTTPCookieProcessor(cookies)
    # 创建opener打开器
    opener = urllib.request.build_opener(cookie_handler)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = opener.open(req)
    html = response.read().decode()
    regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
    str3 = regCom.findall(html)
    # print(str3)
    for reg in str3:
        # print(reg)
        nameCom = re.compile('<h2>(.*?)</h2>', re.S)
        strs1 = nameCom.findall(reg)
        # print(strs1)
        contentCom = re.compile('<span>(.*?)</span>', re.S)
        strs2 = contentCom.findall(reg)
        # print(strs2)
        print("%s 说： %s" % (strs1[0].strip(), strs2[0].strip()))

if __name__ == "__main__":

    # 所有数据
    allData = []
    # [{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},...]

    # 遍历每一页的数据
    for i in range(1, 2):
        url = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
        list1 = getData(url)
        # allData.extend(list1)
        time.sleep(0.5)


    # 遍历allData 把数据显示
    # for dict1 in allData:
    #     print("%s 说： %s" % (dict1["name1"], dict1["content"]))




