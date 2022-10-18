"""
将一个整数分解质因数。例如：输入90,打印出90=233*5。
"""
a = int(0)
inppp = int(input("请输入一个数"))
inpp = int(inppp)
print(inpp,"=",end = '')
for i in range(2,int(inpp/2)):
    a=1
    while a:
        if ((inpp/i) ==int((inpp/i)) and inpp != i):
            inpp /=i
            print(i,"*" ,end='')
        else :
            if (inpp == i or (inpp/i) != int((inpp/i))):
                a=0
if inppp !=inpp:
    print(int(inpp))
else:
    print(1,'*',inppp)
















