def getname(a,b,c,d):
    if(d == 'y'):
        print("Your Full Name is ",a,b,c)
    else:
        print("your full name is ",a,c)

#def getname(a,b):
 #   print("your full name is {} {}".format(a,b))

a=input("enter the first name  ")
b=input("do you have a middle name y/n  ")
y='y'
c=''
if(b==y):
    c=input("middle name  ")
d=input("last name here ")

getname(a,c,d,b)




