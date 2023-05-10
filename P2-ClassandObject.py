class parrot:
    # class attribute
    name: " "
    age: 0


# Parrot1 is an object {created here} and intialize their attribute
parrot1 = parrot()
parrot1.name = "Blu"
parrot1.age = 10

# Parrot2 is an another object {created here} and intialize their attribute
parrot2 = parrot()
parrot2.name = "Rio"
parrot2.age = 5

# Executed the value of the object. Here we understand how to work with object
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")
