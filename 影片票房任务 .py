import re
import bs4
import requests

movie_name = "风平浪静"
sum = [0, 0, 0]
adj = 0
duo = 0
url = "http://72.itmc.org.cn:80/JS001/open/show/box_office_on_a_certain_day.html"
page = requests.get(url=url)
page.encoding = "utf-8"
age = bs4.BeautifulSoup(page.text, "html.parser")

ffind = age.find("tbody", attrs={"class": "table-body"})
names = age.find_all("p")[1:]
piao = age.find_all("div", attrs={"class": "boxDesc-wrap red-color"})
bai = age.find_all("div", attrs={"class": "countRate-wrap"})
for i in range(50):
    names[i] = names[i].text
for i in range(24):
    bai[i] = bai[i].text
    piao[i] = piao[i].text
# 第一个
for i in range(50):
    if movie_name == names[i]:
        if names[i + 1][0:4] == "上映首日":
            sum[0] = 0
            adj = 1
            duo = int(i)
        elif names[i + 1][0:2] == "点映":
            sum[0] = -1
            adj = 1
            duo = int(i)
        elif adj != 1:
            name_n = re.match(r".*?\d+", names[i + 1][2:])
            sum[0] = int(name_n.group())
            duo = int(i)
# 第二个
en = int(duo / 2) - 1
sum[1] = float(piao[en])
# 第三个
try:
    bai[en] = float(re.match(r"\d+.\d+", bai[en]).group())
    sum[2] = bai[en]
except:
    bai[en] = float(re.match(r"\d+.\d+", bai[en][1:]).group())
    sum[2] = bai[en]
sum[2] /= 100
sum[2] = round(sum[2], 4)
print(sum)
