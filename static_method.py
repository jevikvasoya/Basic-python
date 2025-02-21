class vsp():
    def a(self):
        print("hi")
    
    @classmethod
    def b(cls): 
        print('this is class method')

    @staticmethod
    def c(): 
        print('this is static method')

obj = vsp() 
obj.a() # instance method can be called by object

vsp.b() # class method can be called by class name
vsp.c() # static method can be called by class name