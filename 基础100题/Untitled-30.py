"""
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
"""
inpp = str(input("输入一个数"))
if (inpp[0] == inpp[4] and inpp[1] == inpp[3]):
    print("是的")
else:
    print("不是")