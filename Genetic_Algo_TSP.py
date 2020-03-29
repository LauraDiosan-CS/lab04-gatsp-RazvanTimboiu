from Utilitary import *
from GA import *
import time
import keyboard
import matplotlib.pyplot as plt


def search_tsp(file_path, type):
    """
    Cycle searching function for GA TSP
    :param file_path -> path to file where graph is stored
    :param type -> type of graph storage (Coordinates/Roadmap)
    :return -
    """

    combined = {}

    if type == 1:

        print("Working with coordinates...")
        graph = read_graph_coordinates(configure_path(file_path))

        print("Enter population size for selected graph : ")
        ps = int(input())
        print("Enter number of generations for selected graph : ")
        gens = int(input())
        print("Enter mutation rate for selected graph (0.00->0.99) : ")
        mr = float(input())
        print("\nFeel free to press 'q' if the algorithm gets stuck during search...")
        time.sleep(4)

        combined['no_nodes'] = len(graph)
        combined['graph'] = graph

        combined['function'] = euclidean_fitness
        combined['mutation_rate'] = mr
        combined['pop_size'] = ps


    elif type == 2:
        
        print("Working with roadmaps...")
        distance = read_graph_adjacency(configure_path(file_path))

        print("Enter population size for selected graph : ")
        ps = int(input())
        print("Enter number of generations for selected graph : ")
        gens = int(input())
        print("Enter mutation rate for selected graph (0.00->0.99) : ")
        mr = float(input())
        print("\nFeel free to press 'q' if the algorithm gets stuck during search...")
        time.sleep(4)


        combined['no_nodes'] = len(distance)
        print(combined['no_nodes'])
        combined['distance'] = distance

        combined['function'] =  roadmap_fitness
        combined['mutation_rate'] =  mr
        combined['pop_size'] = ps

    ga = GA(combined)
    ga.initialisation()
    ga.evaluation()

    global_best = ga.best_chromosome()

    best = []
    average = []
    best_fitness = -1000

    if combined['function'] ==  roadmap_fitness:
        helper = distance
    else:
        helper = graph

    g = -1
    while(g < gens):
        g += 1
        
        if keyboard.is_pressed("q"):
            break;

        #ga.one_generation()
        #ga.one_generation_elitism()
        ga.one_generation_steady_state()

        fitness_list = [c.fitness for c in ga.population]
        avg_fit = sum(fitness_list) / len(fitness_list)

        average.append(avg_fit)

        local_best = ga.best_chromosome()

        best.append(1 / local_best.fitness)
        
        if local_best.fitness > best_fitness:
           global_best = local_best
           best_fitness = local_best.fitness
            
        print("############## Gen: " + str(g) + " #################")
        print('        Avg fit = ' + str(avg_fit))
        print('Local  Best fit = ' + str(local_best.fitness))
        print('Global Best fit = ' + str(global_best.fitness))
        print('    Best length : ' + str( 1 / (combined['function'](global_best.cicle, helper)) ))
        print('\n')
    print(global_best)

    print("Showing average fit evolution :")
    plt.plot(average)
    plt.ylabel('Average Pop. Fitness')
    plt.xlabel('Generation')
    plt.show()

    plt.plot(best)
    plt.ylabel('Shortest Cicle Lenght')
    plt.xlabel('Generation')
    plt.show()




def small_menu():
    while True:
        print("Choose the dataset you want to search on :")
        print("1: eil51.txt ")
        print("2: fricker26.txt ")
        print("3: berlin52.txt ")
        print("4: st70.txt ")
        print("5: medium8.txt ")
        print("6: Exit")
        cmd = int(input())

        if cmd == 1:
            search_tsp("eil51.txt", 1)
        elif cmd == 2:
            search_tsp("fricker26.txt", 2)
        elif cmd == 3:
            search_tsp("berlin52.txt", 1)
        elif cmd == 4:
            search_tsp("st70.txt", 1)
        elif cmd == 5:
            search_tsp("medium8.txt", 2)
        elif cmd == 6:
            break;




def run():

    small_menu()

run()


