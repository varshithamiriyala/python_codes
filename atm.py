class ATM:
    def __init__(self,name,__pin,c_type):
        self.name=name
        self.__pin=__pin
        self.c_type=c_type
    def __getPin(self):
        print("the pin is:")
        return self.__pin
    def setPin(self,newpin):
        print("pin has changed")
        self.__pin=newpin
bob=ATM('Varshi',1973,'debit')
print(bob.name)
print(bob.setPin(1928))

