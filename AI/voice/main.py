import http.client, urllib, json
from one import sasr_example
from gtts import gTTS
import pygame
import pyttsx3

question = sasr_example().replace("。","")
conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'7a0c7cf0ac4c5ac671b75f4ae8f4aa1b','question':question})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/robot/index',params,headers)
tianapi = conn.getresponse()
result = tianapi.read()
data = result.decode('utf-8')
dict_data = json.loads(data)
answer = dict_data['result']['reply']
answer = answer.replace("<br>", "")
answer = answer.replace("℃", "摄氏度")
answer = answer.replace("~", "到")
answer = answer.replace("-", "负")
print(answer)

"""语言播放方法一"""
'''
tts = gTTS(answer, lang='zh')
tts.save('output.mp3')
pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()
#等待音频播放完成
while pygame.mixer.music.get_busy():
    continue
pygame.mixer.music.stop()
'''

"""语言播放方法二"""
engine = pyttsx3.init()
engine.setProperty('voice', 'zh')
engine.setProperty('rate', 150)    # 设置语速为 150
engine.setProperty('volume', 0.5)  # 设置音量为 0.7
engine.say(answer)
engine.runAndWait()
