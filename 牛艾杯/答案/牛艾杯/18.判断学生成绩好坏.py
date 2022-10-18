print('请输入一个分数：')
score = int(input())
if score >= 90:
    print('A')
else:
    if score >= 60:
        print('B')
    else:
        print('C')