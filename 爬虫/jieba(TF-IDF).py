import requests
import jieba
from jieba import analyse


url = "http://72.itmc.org.cn:80/JS001/data/user/13965/61/fj_chiffon_lady_dress.txt"
resp = requests.get(url)
resp.encoding = "UTF-8"     #中文编码

keywords = jieba.analyse.extract_tags(resp.text, topK=5, withWeight=False, allowPOS=('n', 'nr', 'ns'))
print(keywords)



