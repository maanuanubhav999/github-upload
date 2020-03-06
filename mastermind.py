def separator(b):
    a=[]
    while(int(b)>0):
        a.append(b%10)
        b=b//10
    a.reverse()
    return a

def position(user_input,key):
    a=separator(user_input)
    b=separator(key)
    countpos=0
    for i in range(4):
        if(a[i]==b[i]):
            countpos=countpos+1
    return countpos

def exist(user_input,key):
    a=separator(user_input)
    b=separator(key)
    countany=0
    for i in a:
        if i in b:
            countany=countany+1
    return countany

def duplicate(key):
    #note the elment here may not need to be seperated
    c=0
    key=int(key)
    a=separator(key)
    for i in a:
        if a.count(i)>1:
            #exit condition here
            c=1
    return c
def specificprin(user_input,key):
    print("{} : exist:{}, positioni:{}".format(key,exist(user_input,key),position(user_input,key)))


def guess(user_input,key):
    if(user_input==key):
        print("you have the correct guess")
        return 5

#inputs and all take place here
#user_input=int(input("please enter a 4 word input : "))
#if (user_input.isdigit()) and (len(user_input)==4) and duplicate(user_input)==0):
 #   pass 
count=12
while(True):
    user_input=input("please enter a 4 word input : ")
    if (user_input.isdigit()) and (len(user_input)==4) and (duplicate(user_input)==0):
        while(count>0):
    
            user_key=input("Guess : ")
    
     #checking for the input if it is not repeated and not less than 4 in length  and contains all number
            if (user_key.isdigit()) and (len(user_key)==4 ) and (duplicate(user_key)==0):
             #code for the forward working
                count=count-1
                specificprin(int(user_input),int(user_key))
                c=1
                c=guess(int(user_input),int(user_key))
                if(c==5):
                #print(c)
                    break
            elif(count==1):
                print("you have exhausted all of your chances")
                break
            else:
                print("enter the key again you voilate the rules")
    
        else:
            print("please enter a correct input")

    




#putting the end conditions

