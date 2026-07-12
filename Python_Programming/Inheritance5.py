class Base:

    def fun(self):
        print("Inside Base Fun")

class Derived(Base):
    def sun(self):
        print("Inside dervived Sun")

  
dobj=Derived()
dobj.fun()
dobj.sun()