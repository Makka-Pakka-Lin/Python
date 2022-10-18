import string
a = input()
zimu = 0
kongge = 0
shuzi = 0
qita = 0
for i in a:
    if i.isdigit():
        shuzi +=1
    elif i.isalpha():
        zimu +=1
    elif i.isspace():
        kongge +=1
    else :qita +=1
print(zimu,kongge,shuzi,qita)

