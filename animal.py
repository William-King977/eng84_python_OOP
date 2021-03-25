# Syntax class class_name():

# Creating an Animal class
class Animal():
    # pass # used to bypass the code
    # name = "Dog" # class variable

    def __init__(self): # self refers to the current class instance
        self.alive = True # Attributes / variables
        self.spine = True
        self.lungs = True

    def move(self):
        return "moving, left, right and centre"

    def eat(self):
        return "eating to stay alive"

    def breath(self):
        return "keep breathing to stay alive"

# Creating an object of our Animal class
cat = Animal() # Stores all the data available in the Animal class into cat
oriental_long_hair = Animal()

# print(cat.eat()) # eat is now ABSTRACTED
oriental_long_hair.lungs = False # Polymorphism. Override the value of lungs
print(oriental_long_hair.lungs)