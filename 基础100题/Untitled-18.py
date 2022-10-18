"""
求s=a+aa+aaa+aaaa+aa…a的值，
其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""
s = input("1:")
g = int(input("2:"))
sum = 0
for i in range(g):
    sum+=int(s)
    s+=s[0]
print(sum)
     
