def AND(x1,x2):
    w1,w2 = 0.5,0.5
    theta = 0.7
    tmp = x1 * w1 + x2 * w2
    
    if tmp <= theta:
        return 0
    else:
        return 1
    
    print(AND(1,1))
    print(AND(1,0))
    print(AND(0,0))


def OR(x1,x2):
    w1, w2 = 0.5, 0.5
    theta = 0.2
    tmp = x1 * w1 + x2 * w2
    
    if tmp <= theta:
        return 0
    else:
        return 1







def XOR(x1,x2):
    s1 = not AND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print(XOR(1,1))
print(XOR(1,0))    
print(XOR(0,1))    
print(XOR(0,0))   
    
    