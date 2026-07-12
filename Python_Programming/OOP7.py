class Demo:
    # Class Variables
    Value1=10
    Value2=20

    def __init__(self):
        self.No1=11
        self.No2=21
# Instance Method
    def fun(self):
        print("Inside Instance method named as fun")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)

    @classmethod
    def gun(cls):
        print("Inside Class method named as gun")
        # print(Demo.No1) Not allowed
        # print(Demo.No2) Not allowed
        print(cls.Value1)
        print(cls.Value2)
    
    @staticmethod
    def sun():
        print("Inside Static  method named as sun")
        print(Demo.Value1)
        print(Demo.Value2)

Demo.sun()





