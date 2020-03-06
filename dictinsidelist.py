l=[]
for i in range(30):
    d={'naem':'raj','age':30}
    l.append(d)

for i in range(5):
    print(l[i])

for i in range(3):
    for k,v in l[i].items():
        l[i][k]=3

