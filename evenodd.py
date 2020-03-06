a=int(input("enter a number"))
if(a%2==0):
    for i in range(0,a+1,2):
        print(i, end=" ")
else:
    for i in range(0,a,2):
        print(i,end=" ")

