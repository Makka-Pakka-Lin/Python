import re

import bs4
import requests
from bs4 import BeautifulSoup
# !/usr/bin/env Python
# coding=utf-8

up = [None, 0, 0]
q = 0
n = -1
name = "合众服饰专营店"  # input("输出店名")
url = 'http://72.itmc.org.cn:80/JS001/open/show/ecjd.html'
page = requests.get(url=url)
page.encoding = 'uft-8'
age = bs4.BeautifulSoup(page.text, "html.parser")
for i in range(0, 60):
    names = age.select('#J_goodsList .gl-warp li .J_im_icon a')[i].text
    if name == names:
        # 确认后面
        try:
            to = age.select('#J_goodsList .gl-warp li .p-price')[i].text
            money = float(re.findall(r'\d+\.?\d+', to)[1])
            up[1] = float(money)
            x = i
        except:
            money = float(age.select('#J_goodsList .gl-warp li .p-price strong i')[i].text)
            if money > up[1]:
                x = i
                up[1] = money
# 第二
yesno = age.select('#J_goodsList .gl-warp li .p-icons')[x].text
if '满' in yesno:
    up[0] = True
else:
    up[0] = False
# 第三
people = age.select('#J_goodsList .gl-warp li .p-commit a')[x].text
if "万+" in people:
    try:
        people = float(re.findall(r'\d+\.?\d+', people)[0])
        people *= 10000
    except:
        people = float(re.findall(r'\d+', people)[0])
        people *= 10000
elif '+' in people:
    people = int(re.findall(r'\d+\.?\d+', people)[0])
up[2] = int(people)
print(up)
