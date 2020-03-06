x,e=[int(v),t for v in input()]



def cubesum(x):
    s=0
    for i in range(len(x)):
        s=s+x[i]**3
    return s

q=cubesum(x)
if(x==q):
    print("arm")

