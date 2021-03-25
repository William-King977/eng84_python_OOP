# Python Object Oriented Programming
## What is OOP?
OOP is a programming paradigm that relies on the concept
of classes and objects. It is used to structure a program
into simple, reusable pieces of code blueprints (classes), 
which are used to create individual instances of objects.

### Benefits of OOP
 * OOP models complex code as reproducible and simple 
   structures
 * OOP objects can be used across different programs
 * Class-specific behaviour can be applied through 
   polymorphism
 * Makes it easier to debug programs as they can usually
   be isolated into single classes
 * Protects attributes and methods through encapsulation

## Four pillars of OOP
The four pillars are software design principles that help
you write clean OOP code. The pillars are:

### Abstraction
Abstraction means to hide away the implementation details
inside something from the user. For example, when calling
a function to calculate tax, the user doesn't need to know
how the tax is calculated. This allows code to be reusable
and be more maintainable.

### Encapsulation
Encapsulation is the action of enclosing something in or 
as if in a capsule. In OOP, it is making data private from
the user and controlling its access. It can be used to 
restrict access to certain attributes and methods.

Encapsulation prevents attributes from being modified
unexpectedly, especially when they are overridden, and 
hides away any data that doesn't need to be seen or 
accessed.

### Inheritance
Inheritance is when a class inherits attributes and methods 
from a parent class. For example, there is an Animal class,
and the subclasses include cats, dogs, and sharks. Those
subclasses will share the same attributes and methods from
the Animal class.

The main benefit of inheritance is that it saves you time 
from needing to retype the methods and attributes from 
the parent class.

### Polymorphism
Polymorphism means "many forms", essentially when the 
same thing takes on many forms. This occurs during 
inheritance when the subclasses override the attributes or
methods with their own behaviours.

For example, with a Snake class, a python can inherit from
a snake and share the attributes and methods, such as 
`is_venomous` and `use_venom()`. In this case, because a
python is not venomous, these can be overridden to have
or return values that are suitable for a python.
