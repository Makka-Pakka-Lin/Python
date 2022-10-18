"""
求1+2!+3!+…+20!的和。
"""
sum = 1
sum_all = 0
for i in range(1,21):
    for j in range(1,i+1):
        sum *=j
    sum_all +=sum
    sum = 1
print(sum_all)
