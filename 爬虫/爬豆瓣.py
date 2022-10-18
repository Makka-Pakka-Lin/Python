import re
import requests

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 "
                  "Safari/537.36 "
}
age = requests.get(url, headers=headers)
page_content = age.text

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<fen>.*?)</span>.*?'
                 r'<span>(?P<ren>.*?)</span>', re.S)
result = obj.finditer(page_content)
for it in result:
    print(it.group("name"))
    print(it.group("year").strip())
    print(it.group("fen"))
    print(it.group("ren"))
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()

