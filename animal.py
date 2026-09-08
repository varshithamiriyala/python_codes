class Animal:
    def eat():
        print("it eats")
    def sound():
        print("makes sound")
class Cat(Animal):
    def eat():
        print("cat eats fish")
    def sound():
        print("cat sounds meow")
class Dog(Animal):
    def eat():
        print("dog eats meat")
    def sound():
        print("dog barks")
d1=Dog
d1.sound()
d1.eat()
