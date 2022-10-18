"""
一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
h = 100
sum = 0
h_h = 0
age = 0
for i in range(10):
    sum +=h
    h/=2
    if(i==10):
        age = h
print(sum+100)
print(h)













