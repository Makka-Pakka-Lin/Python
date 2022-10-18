"""
给一个不多于5位的正整数，要求:一、求它是几位数，二、逆序打印出各位数字。
"""
inpp = input("输入一个不多余五位的数")
inpp = str(inpp)
print(len(inpp))
print(inpp[::-1])