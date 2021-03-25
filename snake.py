# Import Reptile class
from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.limbs = False
        self.venom = True
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "smelling for food with my tongue"

    def shed_skin(self):
        return "growing out of my skin"

# Create/Instantiate Snake class
snake_object = Snake()

# print(snake_object.eat()) # eat() inherited from Animal class
# print(snake_object.move()) # move() inherited from Animal class
# print(snake_object.hunt()) # hunt() inherited from Reptile class
# print(snake_object.use_tongue_to_smell()) # from this class

# Multiple inheritance
# Use __method() to make a method private







