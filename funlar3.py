def lar(a,b,c):
    if(a>b):
        if(a>c):
            g=a
        else:
            g=c
    else:
        if(b>c):
            g=b
        else:
            g=c
    return g
n1=int(input("first"))
n2=int(input("second"))
n3=int(input("third"))
print(lar(n1,n2,n3))