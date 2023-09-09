# Classes

class Animal:
    def walk(self):
        print("Walking...")

# Dog class will inherit from Animal Class


class Dog(Animal):
    # init is a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")


roger = Dog("Roger", 5)


print(roger.name)
print(roger.age)

print(roger.bark())
roger.walk()
