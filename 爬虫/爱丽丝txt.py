import requests
import re

url = "http://72.itmc.org.cn:80/JS001/data/user/13965/76/fj_alice_adventure.txt"
name_1 = input("asd:")
name_1 = name_1.lower()
page = requests.get(url=url)
page.encoding = "UTF-8"
age = page.text  # age是txt里的英文文档变量

age = age.lower()
for ch in '!"#$&()*+-,./:;<=>?@[\\]^_{|}·~‘’[\ufeff]':
    age = age.replace(ch, " ")
words = age.split()
counts = {}
for word in words:
    if len(word) >= 3:
        counts[word] = counts.get(word, 0) + 1
    else:
        counts[word] = counts.get(word, 0)
try:
    axd = counts[name_1]
    int(axd)
    print(axd)
except:
    print("0")

