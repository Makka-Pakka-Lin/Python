import requests
import re
from bs4 import BeautifulSoup

name_inpp = input("name:")
url = "http://72.itmc.org.cn:80/JS001/open/show/weixindata.html"
age = requests.get(url)
age.encoding = "utf-8"
q = 0

page = BeautifulSoup(age.text, "html.parser")
tbody = page.find("tbody")
trs = tbody.find_all("span", attrs={"class": "js-rank-detail-btn"})
for tr in trs:
    name = tr.text
    if name == name_inpp:
        tds = tbody.find_all("td")[1:]  # 拿到每行中的所有td
        for i in range(359):
            if (('万' or '万+') in tds[i].text) and ('.' in tds[i].text):
                res = re.findall(r'\d+\.?\d+', tds[i].text)
                tds[i] = int(float(res[0]) * 10000)
            elif ('万' or '万+') in tds[i].text:
                res2 = re.search(r'\d+', tds[i].text)
                tds[i] = int(res2[0]) * 10000
            else:
                try:
                    res3 = re.search(r'\d+', tds[i].text)
                    tds[i] = int(res3[0])
                except:
                    None
        x = 12 * q + 2
        y = 12 * q + 3
        z = 12 * q + 6
        try:
            low = tds[x].text  # .text 表示拿到被标签标记的内容
            avg = tds[y].text  # .text 表示拿到被标签标记的内容
            kind = tds[z].text  # .text 表示拿到被标签标记的内容
            if int(low) < 3000000 and int(avg) > 90000 and int(kind) > 80000:
                print("YES")
            else:
                print("NO")

        except:
            low = tds[x]  # .text 表示拿到被标签标记的内容
            avg = tds[y]  # .text 表示拿到被标签标记的内容
            kind = tds[z]  # .text 表示拿到被标签标记的内容
            if int(low) < 3000000 and int(avg) > 90000 and int(kind) > 80000:
                print("YES")
            else:
                print("NO")

    else:
        q += 1
