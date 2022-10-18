#
#
#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#
#

#1.

a = [1,2,3,4]
b = [0]*100
age = 0
for q_100 in range(0,4):
    for q_10 in range(0,4):
        for q_1 in range(0,4):
            if(a[q_100] !=a[q_10] and a[q_10] !=a[q_1] and a[q_100] != a[q_1] ):
                b[age] = a[q_100]*100+a[q_10]*10+a[q_1]
                print(b[age])
                age += 1
print(age)
"""            

#2.

sum=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if(a!=b and b!=c and a!=c):
                print(a,b,c)
                sum+=1
print(sum)



#3.
from itertools import permutations
a =[1,2,3,4]
sum = 0 
for i in permutations(a,3):
    print(i)
    sum+=1
print(sum)
"""


















