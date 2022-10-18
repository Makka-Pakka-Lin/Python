"""
输入三个整数x,y,z，请把这三个数由小到大输出
摆烂
"""
a_1 = input("1:")
a_2 = input("2:")
a_3 = input("3:")
age = 0
a_sum = [a_1,a_2,a_3]
for x in range(3):
    if(a_1>a_2):
        age = a_1
        a_1 = a_2
        a_2 = age
    if(a_2>a_3):
        age = a_2
        a_2 = a_3
        a_3 = age
    if(a_1>a_3):
        age = a_1
        a_1 = a_3
        a_3 = age
print(a_1)
print(a_2)
print(a_3)









