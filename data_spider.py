"""
@Project: Lottery Prediction
@File: data_spider.py
@Date: 23/01/25
"""
# 爬虫初尝试
# 主要是想运用马尔可夫来预测3D彩票
# 第一步就是要获取历次开奖数据
# 具体参考（通俗易懂）http://t.csdn.cn/7Touk
# 1双色球改为3D
# 2源代码多次fileopen与close，时间过慢（不知道用flush是否能加快速度）
import requests
import os
from bs4 import BeautifulSoup
 
def download(url,page,f):   
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    list = soup.select('div.ball_box01 ul li')
    ball = []
    for li in list:
        ball.append(li.string)
    # print(ball)
    f.write(f'{page},{ball[0]},{ball[1]},{ball[2]}\n')
    f.flush()

def turn_page():
    url = "http://kaijiang.500.com/sd.shtml"
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    pageList = soup.select("div.iSelectList a")
    f = open('3D开奖结果.csv','a',encoding='utf_8_sig')
    for p in pageList:
        url = p['href']
        page = p.string
        download(url,page,f)
    f.close()   
 
def main():
    if(os.path.exists('3D开奖结果.csv')):
        os.remove('3D开奖结果.csv')
    turn_page()


    print(f"录入完成")
if __name__ == '__main__':
    main()
 