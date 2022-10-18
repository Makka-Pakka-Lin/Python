print('输入大于10的数字：')
n = input()
x = str(n)
for i in range(len(x)-1,-1,-1):
    print(x[i])
print('位数是：',len(x))