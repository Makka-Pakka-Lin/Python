"""
有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
"""

mouth_1 = 1     #活了一个月      1->2    2->3    3->4    4>>1
mouth_2 = 0     #活了两个月
mouth_3 = 0     #第三个月开始能生的
mouth_4 = 0     #已经能生的
zhong_2 = 0
zhong_3 = 0
inpp = int(input("几个月"))
for i in range(inpp):
    zhong_2 = mouth_2 
    zhong_3 = mouth_3
    mouth_2 = mouth_1
    mouth_3 = zhong_2
    mouth_4 += zhong_3
    mouth_1 = mouth_4
    print("这个月一共有",mouth_1+mouth_2+mouth_3+mouth_4)



















