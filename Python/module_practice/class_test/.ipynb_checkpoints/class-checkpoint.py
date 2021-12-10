
class Parent:
    def __init__(self, age=8):
        self.attr1 = 123
        self.attr2 = "str"
        self.attr3 = self.func1() #Call func and store return 
        self.age   = age
    
    def func1(self):
        print("Calling func1")
        return 2
    
    def func2(self):
        print("func2")
    
#     def __str__(self):
#         return str(self.attr1)
    
    def __repr__(self):
        return self.attr2
        
    
class Child(Parent):
    def __init__(self, age):
        super().__init__()
        
        
class Parent2:
    def __init__(self, attr1=22, attr2=1, attr3=0, attr4="looking for job", **kwargs):
        self.__dict__.update(**kwargs) #This allows to have as many arguments(with name) as possible
        self.age=attr1
        self.sex =attr2
        self.job = attr3
        self.other = attr4
        
    def func1(self):
        print("Func1s")
        
        
class Child2(Parent2):
    #Now you can have as many arguments as you'd like to have here
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        
        
        