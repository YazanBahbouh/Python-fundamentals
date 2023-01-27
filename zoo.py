class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    
    def add_lion(self, name, age, health_level, mode, species):
        lion = Lion(name, age, health_level, mode, species)
        lion.feed()
        self.animals.append(lion)
    
    def add_octopus(self, name, age, health_level, mode, armsNum):
        octopus = Octopus(name, age, health_level, mode, armsNum) 
        print(octopus.feed())
        self.animals.append(octopus)
    
    def add_bear(self, name, age, health_level, mode, armsNum):
        bear = Bear(name, age, health_level, mode, armsNum) 
        self.animals.append(bear)

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animal:
    def __init__(self,name, age, health_level, mode):
        self.animal_name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = mode

    def feed(self):
        self.health_level = self.health_level + 10
        self.happiness_level = self.happiness_level + 10
        return self

    def display_info(self):
        print("animal info")
        print('animal name',self.animal_name)
        print('animal age',self.age)
        print('animal health',self.health_level)
        print('animal happiness',self.happiness_level)

class Lion(Animal):
    def __init__(self, name, age, health_level, mode, species):
        super().__init__(name, age, health_level, mode)
        self.species = species
    
    def feed(self):
        self.health_level = self.health_level + 15
        return self.health_level

    
    

class Octopus(Animal):
    def __init__(self, name, age, health_level, mode, armsNum):
        super().__init__(name, age, health_level, mode)
        self.arms_num = armsNum
    
    def feed(self):
        return super().feed()
    

class Bear(Animal):
    def __init__(self, name, age, health_level, mode, toothed):
        super().__init__(name, age, health_level, mode)
        self.toothed = toothed
    
    def feed(self):
        self.health_level = self.health_level + 20
        return self.health_level


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Lion", 25, 4, 0, 'mamal')
zoo1.add_octopus("octopus", 10, 3, 6,  8)
zoo1.add_bear("bear", 70, 7, 2, True)
zoo1.print_all_info()
