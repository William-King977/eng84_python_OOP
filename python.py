# Import Snake class
from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False # overriding variable from Snake

    def climb(self):
        return "up we go!"

    def constrict(self):
        return "squeeze prey until they cannot breath"

    # Overriding the method from Reptile
    def use_venom(self):
        return "I don't have venom!"

# Creating an object
python_object = Python()

print(python_object.climb()) # from this class
print(python_object.use_tongue_to_smell()) # from Snake class
print(python_object.hunt()) # from Reptile class
print(python_object.breath()) # from Animal class

# Polymorphism
print(python_object.use_venom())
print(python_object.venom)







