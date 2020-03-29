
import os 
from math import sqrt
from random import randint


def configure_path(filename):
    crtDir =  os.getcwd()
    filePath = os.path.join(crtDir, filename)
    return filePath

def read_graph_coordinates(file_path):
    """
    Utility function to read a graph with format (node x y)
    :param file_path ->pathway to file where graph is stored
    :return dictionary containing key = node and value = [x,y](location)
    """

    file = open(file_path, 'r')
    n = int(file.readline())

    nodes = {}

    for i in range(0, n):
        splits = file.readline().split(' ')
        nodes[int(splits[0]) - 1] = [float(splits[1]), float(splits[2])]

    file.close()

    return nodes


def read_graph_adjacency(file_path):
    """
    Utility function to read a graph's distance matrix
    :param file_path ->pathway to file where graph is stored
    :return distance matrix of the graph it read
    """
    
    file = open(file_path, 'r')
    n = int(file.readline())

    distance = [[0 for i in range(n)] for j in range(n)] 

    for i in range(0, n):
        splits = file.readline().split(',')
        for j in range(0, n):
            distance[i][j] = int(splits[j])

    file.close()

    return distance

def euclidean_distance(one, two):
    """
    Euclidean distance calculator given 2 lists of x,y coordinates of two points
    :param one -> [x,y] of first point
    :param two -> [x,y] of second point
    :return value of euclidean distance between points.
    """
    return sqrt(abs(two[0] - one[0])**2 + abs(two[1] - one[1])**2 )

def euclidean_fitness(cicle, nodes):
    """
    Fitness function for when we're working with node coordinates
    """
    length = 0

    for i in range (0, len(cicle) - 1):
        one = nodes[cicle[i]]
        two = nodes[cicle[i + 1]]
        length += euclidean_distance(one, two)

    return 1 / length

def roadmap_fitness(cicle, distance):
    """
    Fitness function for when we're working with distance matrix
    """
    
    length = 0

    for i in range (0, len(cicle) - 1):
        one = cicle[i]
        two = cicle[i + 1]
        length += distance[one][two]

    return 1 / length

def generate_two(min,max):
    """
    Generates two integers between min and max and returns them in increasing order
    """

    one = randint(min,max)
    two = randint(min,max)

    if one > two:
        return two, one
    else:
        return one, two
