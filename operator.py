class parent:
    def __init__(self,first,last,amount):
        #too assign in object variable
        self.first=first
        self.last=last
        self.amount=amount
        self.full=self.first + self.last
    def makeemail(self):
        return self.first+"."+self.last+"@gmail.com"
    def __add__(self,a):
        return self.amount+a.amount
    def __str__(self):
        return self.first
    def __len__(self):
        return len(self.first)
a=parent('anu','bhav',344)
b=parent('mamu','bhai',88)
print(a.makeemail())
print(b.makeemail())
print(a+b)
print(a) #location will be printed
print(len(a))
