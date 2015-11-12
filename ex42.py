## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog class has a __init__
        ##__init__ has self variable
        ##self variable has got name parameter
        self.name = name

## Cat is an Animal
class Cat(Animal):

    def __init__(self, name):
        ##__init__ has self variable with parameter 'name'
        self.name = name

## The class name is Person
## has a __init__ method and self variable with parameter 'name'
class Person(object):

    def __init__(self, name):
        ##Person's __init__ method with self variable
        ## self variable's got name parameter
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## a variable named self has got a parameter named 'salary'
        self.salary = salary

## Fish is an (Animal object)
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

##  Halibut is a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## mary has a pet called satan
mary.pet = satan

## frank is a employee he has got 120000 salary
frank = Employee("Frank", 120000)

## frank has a rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a kind of salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()
