class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def bark(self):
        print("Bark")
        

d = Dog("Tim", 34)
print(d.get_name())

#OOP2

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())

#OOP3

class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I don't know what to say")

class Cat(pet):
    def speak(self):
        print("Meow")
class Dog(pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Bark")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and my color is {self.color}")

class Fish(pet):
    pass

d = Dog("Tim", 19, "Yellow")
d.show()
d.speak()

c = Cat("Bill", 20)
c.speak()
c.show()

#OOP4

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people +=1

p1 = Person("Tim")
print(Person.number_of_people_())

#OOP5

class Math:

    @staticmethod
    def add5(x):
        return x + 5
    
print(Math.add5(5))


















    







