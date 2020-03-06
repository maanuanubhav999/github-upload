for i in range(int(input())):
    t=input()
    h=len(t)
    if(h%2==0):
        temp1=t[:h//2]
        temp2=t[h//2:]
    else:
        temp1=t[:h//2]
        temp2=t[h//2+1:]
    te1=sorted(temp1)
    te2=sorted(temp2)
    if(te1==te2):
        print("YES")
    else:
        print("NO")
        
