# methods are functions associated with classes or objects
# instance methods :These methods that operate on an instance of a class (i.e objects create from that clas)
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
dog1.bark()