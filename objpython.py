class myclass:
    def __init__(self, name, age, phno):
        self.myName = name
        self.myAge = age
        self.phoneNum = phno

obj = myclass("Akshay",20,9036)
print(type(obj.myName), type(obj.myAge), type(obj.phoneNum))
