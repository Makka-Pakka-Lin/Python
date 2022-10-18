sum=c=0
a,b=1,2
i=1
while i<=20:
    sum += b/a
    a,b=b,a+b
    i+=1
print(sum)