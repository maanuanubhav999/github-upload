class puppy:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

class student(puppy):
    def __init__(self,f,l):
        #to keep the inheritance of the parent's __init__() function add a call to parent's __init__() funtion
        puppy.__init__(self,fname,lname)
        self.fname=f
        self.lname=l

    def pirntss(self):
        self

x=student('mu', 'anu')
x.printname()
