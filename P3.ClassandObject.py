class student:
    def __init__(self, m, s):
        self.math = m
        self.science = s


c1 = student(90, 80)
print(c1.math)
print(c1.science)
print("wihout __str__ function:")
print(c1)


# __init__is a function of all class
# It's a built in function
# Which always executed when the class being initiated

# In this file we initialized the value of of the object


# Note:__init__() functions called automitically everytime the class being used to create a new object


# __str()__ function controls what should be returned when the class object represent as a string

class Address:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}."


c3 = Address("Rayhan", 80)
print("With __str__ Function:")
print(c3)
