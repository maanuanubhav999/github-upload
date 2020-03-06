class collegeid:
    def __init__(self,i):
        self.i=i
    def prints(self):
        print(self.i)

class student(collegeid):
    def __init__(self,i,name):
        super().__init__(i)
        self.name=name
    def printc(self):
        print(self.i,self.name)


n2=student(5,'naman')
collegeid.prints(n2)
student.printc(n2)
