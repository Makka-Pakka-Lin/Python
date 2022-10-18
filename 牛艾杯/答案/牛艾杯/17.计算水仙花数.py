import math
for j in range(100,1000):
    l = str(j)
    if math.pow(int(l[0]),3) + math.pow(int(l[1]),3) + math.pow(int(l[2]),3) == j:
        print(j);