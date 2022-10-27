import re

import requests
import bs4

name = 'Vista看天下'
page = requests.get('http://72.itmc.org.cn:80/JS001/open/show/weixindata.html')
page.encoding = 'utf-8'
page = bs4.BeautifulSoup(page.text, 'html.parser')


def wan(jw):
    if '+' in jw:
        jw = jw[0:-2]
        return int(jw)*10000
    else:
        jw = jw
        return int(jw)


for i in page.select(f'body table.table > tbody > tr'):
    if name == i.find('span', 'js-rank-detail-btn').text:
        tou = i.select(f'td:nth-child(5)')[0].text
        read = i.select(f'td:nth-child(8)')[0].text
        fen = i.select(f'td:nth-child(4)')[0].text
        tou = wan(tou)
        read = wan(read)
        fen = float(fen[0:-1])
        if tou > 90000 and read > 80000 and fen < 300:
            print('YES')
        else:
            print('NO')
