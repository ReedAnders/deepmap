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
