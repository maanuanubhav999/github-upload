class addition:
    first=0
    second=0
    answer=0

    #perameterized constructor
    def __init__(self,f,s):
        self.first=f
        self.second=s

    def display(self):
        print(self.first)
        print(self.second)
        print(self.answer)

    def cal(self):
        self.answer=self.first + self.second

obj=addition(1000,500)
obj.cal()
obj.display()
