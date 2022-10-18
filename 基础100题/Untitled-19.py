"""
一个数如果恰好等于它的因子之和，
这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
#这个是输入一个数看是不是是全数
inpp = int(input("输入数"))
inppp = inpp
ang = [1]
sum = 0
for i in range(2,inpp):
    a=1
    while a:
        if ((inpp/i) ==int((inpp/i)) ):
            inpp /=i
            ang.append(i)
        else :
            if (inpp == i or (inpp/i) != int((inpp/i))):
                a=0
for j in range(0,len(ang)):
    sum += ang[j]

print(ang)
if sum == inppp:
    print("ok")
else:
    print("NO")
"""

ang = [1]
sum = 0
j = int(0)
for x in range(6,1000):
    for i in range(2,x):
        if (x%i == 0):
            ang.append(i)

    for j in range(0,len(ang)):
        sum += ang[j]
    if sum == x:
        print(sum)
    sum = 0
    ang = [1]
    















