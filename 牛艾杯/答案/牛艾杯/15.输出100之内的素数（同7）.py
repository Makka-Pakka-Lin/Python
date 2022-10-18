for i in range (0,101):
    if i >1:
        for j in range (2,i):
            if i%j == 0:
                break 
                
        else :
            print('{0}是素数',i)
