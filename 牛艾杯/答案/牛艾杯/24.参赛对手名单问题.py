A = ['x','y','z']
B = ['x','y','z']
C = ['x','y','z']
for a in A:
    for b in B:
        for c in C:
            if a!=b!=c!=a and c!='x' and c!='z' and a!='x':
                print ("a和{0}比，b和{1}比，c和{2}比".format (a,b,c))
