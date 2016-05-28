# -*- coding: utf-8 -*-

# http://nbviewer.jupyter.org/github/lmarti/evolutionary-computation-course/blob/master/AEC.03%20-%20Solving%20the%20TSP%20with%20GAs.ipynb

import os
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib
import random
import operator
import itertools
import numpy
import math
from time import perf_counter, time

random.seed(time())  # planting a random seed


def exact_TSP(cities):
    "Generate all possible tours of the cities and choose the shortest one."
    return shortest(alltours(cities))


def shortest(tours):
    "Return the tour with the minimum total distance."
    return min(tours, key=total_distance)

# The permutation function is already defined in the itertools module
alltours = itertools.permutations
cities = {1, 2, 3}
list(alltours(cities))


def total_distance(tour):
    "The total distance between each pair of consecutive cities in the tour."
    return sum(distance(tour[i], tour[i - 1])
               for i in range(len(tour)))

City = complex  # Constructor for new cities, e.g. City(300, 400)


def distance(A, B):
    "The Euclidean distance between two cities."
    return abs(A - B)

A = City(300, 0)
B = City(0, 400)
distance(A, B)


def generate_cities(n):
    "Make a set of n cities, each with random coordinates."
    return set(City(random.randrange(10, 890),
                    random.randrange(10, 590))
               for c in range(n))

cities8, cities10, cities100, cities1000 = generate_cities(
    8), generate_cities(10), generate_cities(100), generate_cities(1000)
cities8


def plot_tour(tour, alpha=1, color=None):
    # Plot the tour as blue lines between blue circles, and the starting city
    # as a red square.
    plotline(list(tour) + [tour[0]], alpha=alpha, color=color)
    plotline([tour[0]], 'rs', alpha=alpha)
    # plt.show()


def plotline(points, style='bo-', alpha=1, color=None):
    "Plot a list of points (complex numbers) in the 2-D plane."
    X, Y = XY(points)

    if color:
        plt.plot(X, Y, style, alpha=alpha, color=color)
    else:
        plt.plot(X, Y, style, alpha=alpha)


def XY(points):
    "Given a list of points, return two lists: X coordinates, and Y coordinates."
    return [p.real for p in points], [p.imag for p in points]

tour = exact_TSP(cities8)
plot_tour(tour)


def all_non_redundant_tours(cities):
    "Return a list of tours, each a permutation of cities, but each one starting with the same city."
    start = first(cities)
    return [[start] + list(tour)
            for tour in itertools.permutations(cities - {start})]


def first(collection):
    "Start iterating over collection, and return the first element."
    for x in collection:
        return x


def exact_non_redundant_TSP(cities):
    "Generate all possible tours of the cities and choose the shortest one."
    return shortest(all_non_redundant_tours(cities))

all_non_redundant_tours({1, 2, 3})

top = perf_counter()
exact_TSP(cities8)
print(top - perf_counter(), 's')
top = perf_counter()
exact_non_redundant_TSP(cities8)
print(top - perf_counter(), 's')
top = perf_counter()
exact_non_redundant_TSP(cities10)
print(top - perf_counter(), 's')


def greedy_TSP(cities):
    "At each step, visit the nearest neighbor that is still unvisited."
    start = first(cities)
    tour = [start]
    unvisited = cities - {start}
    while unvisited:
        C = nearest_neighbor(tour[-1], unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour


def nearest_neighbor(A, cities):
    "Find the city in cities that is nearest to city A."
    return min(cities, key=lambda x: distance(x, A))

cities = generate_cities(9)
top = perf_counter()
exact_non_redundant_TSP(cities)
print(top - perf_counter(), 's')
plot_tour(exact_non_redundant_TSP(cities))

top = perf_counter()
greedy_TSP(cities)
print(top - perf_counter(), 's')
plot_tour(greedy_TSP(cities))

top = perf_counter()
greedy_TSP(cities100)
print(top - perf_counter(), 's')
plot_tour(greedy_TSP(cities100))

top = perf_counter()
greedy_TSP(cities1000)
print(top - perf_counter(), 's')
plot_tour(greedy_TSP(cities1000))

from deap import algorithms, base, creator, tools

num_cities = 30
cities = generate_cities(num_cities)
toolbox = base.Toolbox()

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox.register("indices", numpy.random.permutation, len(cities))
toolbox.register("individual", tools.initIterate, creator.Individual,
                 toolbox.indices)
toolbox.register("population", tools.initRepeat, list,
                 toolbox.individual)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)


def create_tour(individual):
    return [list(cities)[e] for e in individual]


def evaluation(individual):
    '''Evaluates an individual by converting it into
    a list of cities and passing that list to total_distance'''
    return (total_distance(create_tour(individual)),)

toolbox.register("evaluate", evaluation)
toolbox.register("select", tools.selTournament, tournsize=3)

pop = toolbox.population(n=100)

result, log = algorithms.eaSimple(pop, toolbox,
                                  cxpb=0.8, mutpb=0.2,
                                  ngen=400, verbose=False)

best_individual = tools.selBest(result, k=1)[0]
print('Fitness of the best individual: ', evaluation(best_individual)[0])

plot_tour(create_tour(best_individual))
fit_stats = tools.Statistics(key=operator.attrgetter("fitness.values"))
fit_stats.register('mean', numpy.mean)
fit_stats.register('min', numpy.min)

result, log = algorithms.eaSimple(toolbox.population(n=100), toolbox,
                                  cxpb=0.5, mutpb=0.2,
                                  ngen=400, verbose=False,
                                  stats=fit_stats)

plt.figure(1, figsize=(11, 4), dpi=500)
plots = plt.plot(log.select('min'), 'c-',
                 log.select('mean'), 'b-', antialiased=True)
plt.legend(plots, ('Minimum fitness', 'Mean fitness'))
plt.ylabel('Fitness')
plt.xlabel('Iterations')

pop_stats = tools.Statistics(key=numpy.copy)
pop_stats.register('pop', numpy.copy)  # -- copies the populations themselves
pop_stats.register('fitness',  # -- computes and stores the fitnesses
                   lambda x: [evaluation(a) for a in x])

result, log = algorithms.eaSimple(toolbox.population(n=100), toolbox,
                                  cxpb=0.5, mutpb=0.2,
                                  ngen=400, verbose=False,
                                  stats=pop_stats)


def plot_population(record, min_fitness, max_fitness):
    '''
    Plots all individuals in a population.
    Darker individuals have a better fitness.
    '''
    pop = record['pop']
    fits = record['fitness']
    index = sorted(range(len(fits)), key=lambda k: fits[k])

    norm = colors.Normalize(vmin=min_fitness,
                            vmax=max_fitness)
    sm = cmx.ScalarMappable(norm=norm,
                            cmap=plt.get_cmap('PuBu'))

    for i in range(len(index)):
        color = sm.to_rgba(max_fitness - fits[index[i]][0])
        plot_tour(create_tour(pop[index[i]]), alpha=0.5, color=color)

min_fitness = numpy.min(log.select('fitness'))
max_fitness = numpy.max(log.select('fitness'))

plt.figure(1, figsize=(11, 11), dpi=500)
for i in range(0, 12):
    plt.subplot(4, 3, i + 1)
    it = int(math.ceil((len(log) - 1.) / 15))
    plt.title('t=' + str(it * i))
    plot_population(log[it * i], min_fitness, max_fitness)

top = perf_counter()
total_distance(greedy_TSP(cities))
print(top - perf_counter(), 's')

print('greedy_TSP() distance: ', total_distance(greedy_TSP(cities)))
print('Genetic algorithm best distance: ', evaluation(best_individual)[0])

os.system("pause")
