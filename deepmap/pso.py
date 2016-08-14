from optparse import OptionParser
from random import random
from math import sin, sqrt
import numpy as np

import swarm

# MAKE MODULAR
def f6(param):
    '''Schaffer's F6 function'''
    para = param*10
    para = param[0:2]
    num = (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) * \
        (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) - 0.5
    denom = (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1]))) * \
            (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1])))
    f6 =  0.5 - (num/denom)
    errorf6 = 1 - f6
    return f6, errorf6;

# PSO Algorithm
def pso(swarm, iter_max=100000, err_crit = 0.00001, index=1):

    # err = 999999999

    while index < iter_max:

        for p in swarm.population:
            fitness, err = f6(p.params)

            if fitness > p.fitness:
                p.fitness = fitness
                p.pBest = p.params

            if fitness > swarm.gBestFitness:
                swarm.gBestSolution = p.params
                swarm.gBestFitness = p.fitness

            v = p.v + sw.c1 * random() * (p.pBest - p.params) \
                    + sw.c2 * random() * (swarm.gBestSolution - p.params)

            p.params = p.params + v

            index += 1

        if err < err_crit:
            break

        #progress bar. '.' = 10%
        if index % (iter_max/10) == 0:
            print '.'

    print 'RESULTS\n', '-'*7
    print 'gbest fitness   : ', swarm.gBestFitness
    print 'gbest params    : ', swarm.gBestSolution
    print 'iterations      : ', index

# MAIN
if __name__ == "__main__":

    sw = swarm.Swarm(population_size=1000)

    pso(sw)
