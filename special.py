def speci(n):
    a=n
    j=a
    b=0
    su=0
    temp=1
    while(a>0):
        b=a%10
        su=su + b
        temp=temp*b
        a=a//10
    temp2=temp+su
    if(temp2==j):
        return True
    else:
        return False



q=int(input("please enter a number"))
print(speci(q))



