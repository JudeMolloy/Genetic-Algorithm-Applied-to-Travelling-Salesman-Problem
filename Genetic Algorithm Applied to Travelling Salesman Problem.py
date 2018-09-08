'''
 Application of a Genetic Algorithm on the Travelling Salesman Problem
 Developed by Jude Molloy
 Work started 31/08/2018
'''


import math
import random
from copy import deepcopy

# location data as coordinates

locationData = [[1, 10], [4, 23], [2, 3], [8, 5], [16, 18]]

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#   def getX(self):
 #       return self.x

 #   def getY(self):
  #      return self.y


class Route:
    def __init__(self):
        self.fitness = 0

    path = set()


class Population:
    def __init__(self):
        self.population = []

    # generates a genetic representation of the domain
    def generatePopulation(self, populationSize):
        '''converts all of the lists in the population into tuples (as tuples are hashable) so the
        population can be casted to a set'''
        self.population = set(map(tuple, self.population))
        while len(self.population) < populationSize:
            route = Route()
            while len(route.path) < numberOfLocations:
                route.path.add(random.randint(0, numberOfLocations - 1))
            # must convert to a list as tuples and sets are immutable and the order must be shuffled
            route.path = list(route.path)
            random.shuffle(route.path)
            self.population.add(route)
        self.population = list(self.population)
        return self.population

    def calculateFitness(self, route):
        totalDistance = 0
        if self.population[route].fitness == 0:
            path = self.population[route].path
            for i in range(len(path)):
                if i + 1 == len(path):
                    totalDistance += calculateDistanceBetween(path[i], path[0])
                else:
                    totalDistance += calculateDistanceBetween(path[i], path[i + 1])
            self.population[route].fitness = totalDistance
        return totalDistance

    def evolve(self, numberOfSurvivors, numberOfGenerations, mutatedGenes):
        for i in range(len(self.population)):
            self.calculateFitness(i)
        while numberOfGenerations > 0:
            self.survivalOfTheFittest(numberOfSurvivors)
            self.mutate(mutatedGenes)
            for i in range(len(self.population)):
                self.calculateFitness(i)
            numberOfGenerations -= 1
        self.population = quicksortPopulation(self.population)
        solution = self.population[0]
        return solution

    def survivalOfTheFittest(self, numberOfSurvivors):
        quicksortPopulation(self.population)
        self.population = quicksortPopulation(self.population)[0:numberOfSurvivors]
        return self.population

    '''
    small mutation rate due to what I read on
    https://www.researchgate.net/post/Why_is_the_mutation_rate_in_genetic_algorithms_very_small
    '''
    def mutate(self, mutatedGenes):
        '''
        Creating another 2 copies of each gene/path to allow for more mutation with the fittest genes.
        Also the a copy of the fittest will not be mutated to allow for the fittest to always remain.
        '''

        mutation = deepcopy(self.population) + deepcopy(self.population)
        # randomly mutate the genes (route.path = gene). Switches 2 of the locations in the path.
        def performMutation(mutatedGenes):
            while mutatedGenes > 0:
                for route in mutation:
                    route.fitness = 0
                    index1 = random.randint(0, len(route.path) - 1)
                    index2 = index1
                    while index2 == index1:
                        index2 = random.randint(0, len(route.path) - 1)
                    temp = int()
                    temp = route.path[index1]
                    route.path[index1] = route.path[index2]
                    route.path[index2] = temp
                mutatedGenes -= 1

        performMutation(mutatedGenes)

        self.population = self.population + mutation
        for x in self.population:
            print(x.path)





def calculateDistanceBetween(location1, location2):
    print(location2)
    xDistance = locations[location1].x - locations[location2].x
    yDistance = locations[location1].y - locations[location2].y
    distance = math.sqrt(((xDistance) ** 2) + ((yDistance) ** 2))
    return distance


def quicksortPopulation(list):
    less = []
    equal = []
    greater = []

    if len(list) > 1:
        pivot = list[0].fitness
        for route in list:
            if route.fitness < pivot:
                less.append(route)
            elif route.fitness > pivot:
                greater.append(route)
            else:
                equal.append(route)
        list = quicksortPopulation(less) + equal + quicksortPopulation(greater)
        return quicksortPopulation(less) + equal + quicksortPopulation(greater)
    else:
        return list








locations = []

numberOfLocations = 5

locations.append(Location(1, 2))
locations.append(Location(3, 5))
locations.append(Location(5, 4))
locations.append(Location(6, 6))
locations.append(Location(9, 6))
locations.append(Location(17, 19))



test = Population()
test.generatePopulation(3)

# def evolve(self, numberOfSurvivors, numberOfGenerations, mutatedGenes):
solution = test.evolve(2, 3, 2)
print(solution.fitness)
print(solution.path)

