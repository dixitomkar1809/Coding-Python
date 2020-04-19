# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and6780- dequeueCat. You may use the built-in Linkedlist data structure
'''
import datetime

secondsInADay = 24 * 60 * 60

class Animal:
    def __init__(self, type, order):
        self.type = type
        self.order = order

    def getOrder(self):
        return self.order

    def getType(self):
        return self.type

class AnimalShelter:
    def __init__(self):
        self.animalQueue = []
        self.dogs = []
        self.cats = []

    def enqueueDog(self, dog):
        self.dogs.append(dog)

    def dequeueDog(self):
        if len(self.dogs):
            return self.dogs.pop(0)
        return None

    def enqueueCat(self, cat):
        self.cats.append(cat)

    def dequeueCat(self):
        if len(self.cats):
            return self.cats.pop(0)
        return None

    def dequeueAnimal(self):
        if not len(self.dogs) and not len(self.cats):
            return None
        elif not len(self.cats):
            return self.dogs.pop(0)
        elif not len(self.dogs):
            return self.cats.pop(0)
        else:
            dog = self.dogs[0]
            cat = self.cats[0]
            dogOrder = dog.getOrder()
            catOrder = cat.getOrder()
            if (dogOrder < catOrder):
                self.dogs.pop(0)
                return dog
            else:
                self.cats.pop(0)
                return cat

    def enqueueAnimal(self):
        animal = self.dequeueAnimal()
        if animal:
            self.animalQueue.append(animal)
            return True
        print("No Animals!")
        return False

    def printQueue(self):
        for animal in self.animalQueue:
            print(animal.getType(), animal.getOrder())
            
if __name__=="__main__":
    animalShelter = AnimalShelter()
    dog1 = Animal("dog", 1)
    dog2 = Animal("dog", 3)
    dog3 = Animal("dog", 5)
    cat1 = Animal("cat", 2)
    cat2 = Animal("cat", 4)
    cat3 = Animal("cat", 6)
    animalShelter.enqueueCat(cat1)
    animalShelter.enqueueCat(cat2)
    animalShelter.enqueueCat(cat3)
    animalShelter.enqueueDog(dog1)
    animalShelter.enqueueDog(dog2)
    animalShelter.enqueueDog(dog3)
    animalShelter.enqueueAnimal()
    animalShelter.enqueueAnimal()
    animalShelter.enqueueAnimal()
    animalShelter.enqueueAnimal()
    animalShelter.printQueue()
