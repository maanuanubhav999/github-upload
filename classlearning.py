class human():
    name=" rama"
    age=0
    #these values here could be accessed by using constructor
    hetight=173
    aadhar="dfdf"
    #method , no argumetnt need to be give
    def printdetails(self):
        print(self.name ,self.age ,self.aadhar)
    def __init__(self,name,age):
        #print(self.name,self.age)
        self.name=name
        self.age=age
        

#creation of object of class = obj_name=classname
obj=human("anubh",34)
#obj.name="anub"
#obj.age=34

#obj.aadhar="3f33"
obj.printdetails()

#it will start to take default vaule is not given
