from random import randint, shuffle
from Chromosome import *

class GA:
    def __init__(self, param = None):
        self.__param = param
        self.__population = []

    @property
    def population(self):
        return self.__population


    def initialisation(self):

        list = [i for i in range(1, self.__param['no_nodes'])]

        for _ in range(0, self.__param['pop_size']):
            shuffle(list)
            init = [0] + list + [0]

            c = Chromosome(self.__param)
            c.cicle = init
            self.__population.append(c)


    def evaluation(self):

        if self.__param['function'] == euclidean_fitness:

            for c in self.__population:
                c.fitness = self.__param['function'](c.cicle,self.__param['graph'])

        else :

            for c in self.__population:
                c.fitness = self.__param['function'](c.cicle,self.__param['distance'])
            

    def best_chromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best


    def selection(self):
        one = randint(0, self.__param['pop_size'] - 1)
        two = randint(0, self.__param['pop_size'] - 1)
        if self.__population[one].fitness > self.__population[two].fitness:
            return one
        else:
            return two


    def one_generation(self):
        new_pop = []
        for _ in range(self.__param['pop_size']):
            one = self.__population[self.selection()]
            two = self.__population[self.selection()]
            off = one.crossover(two)
            off.mutate()
            new_pop.append(off)
        self.__population = new_pop
        self.evaluation()


    def one_generation_elitism(self):
        new_pop = [self.best_chromosome()]
        for _ in range(self.__param['pop_size'] - 1):
            one = self.__population[self.selection()]
            two = self.__population[self.selection()]
            off = one.crossover(two)
            off.mutate()
            new_pop.append(off)
        self.__population = new_pop
        self.evaluation()


    def one_generation_steady_state(self):
        self.__population = sorted(self.__population, key=lambda x: x.fitness, reverse=True)

        for _ in range(self.__param['pop_size']):
            one = self.__population[self.selection()]
            two = self.__population[self.selection()]
            off = one.crossover(two)
            off.mutate()

            if self.__param['function'] == euclidean_fitness:

                off.fitness = self.__param['function'](off.cicle, self.__param['graph'])
            else:
                off.fitness = self.__param['function'](off.cicle, self.__param['distance'])

            if off.fitness > self.__population[-1].fitness:
                self.__population[-1] = off
        self.evaluation()
