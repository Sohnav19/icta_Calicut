def rev(num):
    re=0
    while(num>0):
        r=num%10
        re=(re*10)+r
        num=num//10
    return re
a=int(input("Enter the number"))
print(rev(a))