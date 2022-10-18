"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""

string = input("输入字符串：")
spa = 0
num = 0
alp = 0
oth = 0

for i in range(len(string)):
    if string[i].isspace():
        spa+=1
    elif string[i].isdigit():
        num+=1
    elif string[i].isalpha():
        alp+=1
    else:
        oth+=1

print(spa)
print(num)
print(alp)
print(oth)
