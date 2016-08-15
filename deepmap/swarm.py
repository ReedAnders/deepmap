# Copyright (C) 2016 Reed Anderson.
# From: https://github.com/ReedAnders/deepmap
# License: MIT BY https://opensource.org/licenses/MIT

import numpy as np
from random import random

# Initialize particle parameters randomly
class Particle:
	def __init__(self, dimensions=2):
		self.dimensions = dimensions
		self.params = np.array([random() for i in range(dimensions)])
		self.fitness = 0.0
		self.v = 0.0
		self.pBest = self.params

	def __repr__(self):
		return 'Particle(dimensions=%r, params=%r, fitness=%r, pBest=%r)' \
            % (self.dimensions, self.params, self.fitness, self.pBest)

# Initialize swarm list of class Particle
class Swarm:
    def __init__(self, population_size=120, dimensions=2, c1=2, c2=2):
        self.population = [Particle(dimensions=dimensions) for particle in range(population_size)]
        self.population_size = population_size
        self.c1 = c1
        self.c2 = c2
        self.gBestSolution = None
        self.gBestFitness = None

    def __repr__(self):
        return 'Swarm(population_size=%r, gBestFitness=%r)' \
            % (self.population_size, self.gBestFitness)

# Metaheuristic optmization methods
class PSO:
    def __init__(self, iter_max=100000, err_crit = 0.000001):
        self.iter_max = iter_max
        self.err_crit = err_crit

    def optimize(self, func, swarm, index=1):

        while index < self.iter_max:

            for p in swarm.population:
                fitness, err = func(p.params)

                if fitness > p.fitness:
                    p.fitness = fitness
                    p.pBest = p.params

                if fitness > swarm.gBestFitness:
                    swarm.gBestSolution = p.params
                    swarm.gBestFitness = p.fitness

                v = p.v + swarm.c1 * random() * (p.pBest - p.params) \
                        + swarm.c2 * random() * (swarm.gBestSolution - p.params)

                p.params = p.params + v

                index += 1

            if err < self.err_crit:
                break

            #progress bar. '.' = 10%
            if index % (self.iter_max/10) == 0:
                print '.'

        print 'RESULTS\n', '-'*7
        print 'gbest fitness   : ', swarm.gBestFitness
        print 'gbest params    : ', swarm.gBestSolution
        print 'iterations      : ', index
