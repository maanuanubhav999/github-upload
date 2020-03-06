class parent:
    def fun(self,make,shl):
        print(int(make)+int(shl))

class child(parent):
    def fun(self,make,shl):
        print(make*shl)
    def run(self,make,sh):
        parent.fun(self,make,shl)
c=child()
c.fun(23,2)
c.run(23,2)
