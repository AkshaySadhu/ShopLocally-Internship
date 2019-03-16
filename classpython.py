class elonmusk:
    def __init__(self):
        self.car =  input("Which car do you want??")
        if self.car == "Model S":
            self._teslaS()
        elif self.car == "Model 3":
            self._tesla3()
        elif self.car == "Model X":
            self._teslaX()
        else:
            print("Car Doesn't exist")
    def _teslaS(self):
        print("It will cost you two crap loads")
    def _tesla3(self):
        print("It will cost you one crap load")
    def _teslaX(self):
        print("It will cost you three crap loads")
    

elonmusk()
