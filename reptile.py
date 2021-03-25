# import Animal class
from animal import Animal

class Reptile(Animal): # we need to pass the animal class as an arg in our Reptile class

    def __init__(self):
        super().__init__() # makes everything available from parent class
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]

    def hunt(self):
        return "catch their next meal"

    def use_venom(self):
        return "use venom if I got it"

    def seek_heat(self):
        return "looking for sunshine"

# Demonstrating Inheritance
# reptile_object = Reptile()
# # Magic of OOP
# print(reptile_object.hunt())
# print(reptile_object.breath())
