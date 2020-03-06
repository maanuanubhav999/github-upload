class car:
    def __init__(self,make , model ,year):
        self.make=make
        self.model=model
        self.year=year
    def printDetails(self):
        print(self.make)
        print(self.model)
        print(self.year)
    

class horsepower:
    def __init__(self,engine):
        self.engine=engine
    def turbo(self):
        print(self.engine)

class electric(car,horsepower):
    def __init__(self,make,model,year,charge,engine):
        car.__init__(self,make,model,year)    #super()__init__(self,make,model,year)
        horsepower.__init__(self,engine)
       # self.engine=engine
        self.charge=charge
    def charging(self):
        print(self.charge)
        print(self.make)
        print(self.model)
        print(self.engine)

p1=car('johh','mustang',2020)
p1.printDetails()

p2=electric('po','lota',4004,'full','supercharge')
p2.charging()

