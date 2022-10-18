l = [8,1,3,7,9,2]
max = 0
min = len(l)
for i in range(0,len(l)):
    if l[i]>max:
        max = l[i]
        maxpt = i
    if l[i]<min:
        min = l[i]
        minpt = i
zancun = l[0]
l[0] = max
l[maxpt] = zancun
zancun = l[len(l)-1]
l[len(l)-1] = min
l[minpt] = zancun
print(l)