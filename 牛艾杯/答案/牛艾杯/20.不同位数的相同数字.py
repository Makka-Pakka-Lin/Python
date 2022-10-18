a = c =input('输入一个数')
b = input('输入相加的次数')
s = int(a)
for i in range(0,int(b)-1):
    c = int (a) + int (c)*10
    s += c
print(s)
