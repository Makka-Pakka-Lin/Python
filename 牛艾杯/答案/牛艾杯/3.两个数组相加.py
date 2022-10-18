#请输入代码
d = [8,13,7,9,2]
for i in range(len(d)):
    if d[i] == max(d):
        d[i],d[0] = d[0],d[i]
for j in range(len(d)):
    if d[i] == min(d):
        d[i],d[4] = d[4],d[i]
print(d)
