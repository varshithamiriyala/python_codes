class Electronics:
    def turnOn():
        print('device is on')
class Mobile(Electronics):
    def takePics():
        print('clicked pics')
poco=Mobile
poco.turnOn()
poco.takePics()
