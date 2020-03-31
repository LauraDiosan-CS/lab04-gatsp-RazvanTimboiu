from random import randint, random
from Utilitary import *

class Chromosome:
    def __init__(self, param=None):
        self.__param = param
        self.__genes = []
        self.__fitness = 0.0

    @property
    def cicle(self):
        return self.__genes

    @cicle.setter
    def cicle(self, cicle = []):
        self.__genes = cicle

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, other):
        
        one, two = generate_two(1, len(self.__genes) - 2)

        A = self.__genes[one: two + 1]
        B = [gene for gene in other.__genes if gene not in A]

        B[one:one] = A

        off = Chromosome(self.__param)
        off.cicle = B
        return off


    def mutate(self):

        #for _ in range(1, len(self.__genes) - 1):

        chance = random()
        if chance < self.__param['mutation_rate']:
             one, two = generate_two(1, len(self.__genes) - 2)
             self.__genes[one: two + 1] = self.__genes[one: two + 1][::-1]


    def __str__(self):
        return '\nCicle: ' + str(self.__genes) + ' has length : ' + str(1/self.__fitness)

