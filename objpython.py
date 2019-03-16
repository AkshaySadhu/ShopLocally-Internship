class myclass:
    def __init__(self, name, age, phno):
        self.myName = name
        self.myAge = age
        self.phoneNum = phno
    @property
    def name(self):
        return self.myName
    @name.setter
    def name(self, name):
        self.myName = name
        
    
obj = myclass("Akshay",20,9036)
print(type(obj.myName), type(obj.myAge), type(obj.phoneNum))
print(obj.name())
obj.name("Bleh")
print(obj.name())
