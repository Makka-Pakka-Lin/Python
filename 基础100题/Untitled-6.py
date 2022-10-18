"""
斐波那契数列   输入几输出第几个数
1,1,2,3,5,8,13,21,34,55,89
"""

a = 1
b = 1
c=0
xyz = int(input("第几个数："))
for i in range(xyz-2):
    c = b 
    b = a+b
    a = c
print(b)

