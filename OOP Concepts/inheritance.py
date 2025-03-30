# it is a concept where classes inherit attributes and methods from other classes

#Example lets have a parent class of animal and sub classes of prey and predator


class Animal:
    def __init__(self,name):
        self.name = name;
    def description(self):
        print("It is animal.")
class Prey(Animal):
    def fleeing(self):
        print(f"{self.name} is fleeing");
class Predator(Animal):
    def description(self):
        print(f"{self.name} is a wild animal.")
        # This concept is called method overiding where a child shares a method with the parent. The program uses the childs version

        super().description() # to use the parent version of the method.
    def hunting(self):
        print(f"{self.name} is hunting");

class Lion(Predator):
    pass
class Deer(Prey):
    pass
class Fish(Predator, Prey):
    pass

lion=Lion("Simba");
deer =Deer("Pookie");
fish = Fish("Nimo")

lion.description();
lion.hunting();