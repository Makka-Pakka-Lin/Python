"""
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
"""
inpp = str(input("输入一到俩"))
if len(inpp) == 1:
    if      inpp[0] == 'M':
        print('1')
    elif    inpp[0] =='W':
        print('3')
    elif    inpp[0] =='F':
        print('5')
    else :
        print("请注意开头大小写或者拼写")
elif len(inpp) == 2:
    if      (inpp[0] == 'T' and inpp[1] == 'u'):
        print('2')
    elif    (inpp[0] == 'T' and inpp[1] == 'h'):
        print('4')
    elif    (inpp[0] == 'S' and inpp[1] == 'a'):
        print('6')
    elif    (inpp[0] == 'S' and inpp[1] == 'u'):
        print('7')
    else :
        print("请注意开头大小写或者拼写")
else :
    print("请注意开头大小写或者拼写")