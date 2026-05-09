class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(f"My name is {self.name}.")
x = Person("John", 36)
x.printname()  # Output: My name is John.


# There going Inheritance
class Student(Person):
  pass
x = Student("Mike", 20)
x.printname()  # Output: My name is Mike.