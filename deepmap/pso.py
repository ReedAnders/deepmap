from random import random

import swarm
# from f6 import f6
import benchmark

# PSO Algorithm
def pso(func, swarm, iter_max=100000, err_crit = 0.000001, index=1):

    while index < iter_max:

        for p in swarm.population:
            fitness, err = func(p.params)

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


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(description='Run PSO on a benchmark')
    parser.add_argument('--pop', default=120, type=int,
                        help='swarm population size')
    parser.add_argument('--d', default=2, type=int,
                        help='solution dimension size')
    parser.add_argument('--c', default=2.0, type=float,
                        help='particle acceration constant')
    parser.add_argument('--err_crit', default=0.00001, type=float,
                        help='error criteria for stopping PSO')
    parser.add_argument('--iter_max', default=1000, type=float,
                        help='maximum iterations for stopping PSO')
    args = parser.parse_args()

    sw = swarm.Swarm(population_size=args.pop, \
                        dimensions=args.d, c1=args.c, c2=args.c)

    func = benchmark.Benchmark().f6
    # func = f6

    pso(func, sw, iter_max=args.iter_max, err_crit=args.err_crit)
