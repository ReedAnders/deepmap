# Copyright (C) 2016 Reed Anderson.
# From: https://github.com/ReedAnders/deepmap
# License: MIT BY https://opensource.org/licenses/MIT

from random import random
import argparse

import swarm
import benchmark
import nn

def main():

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

    # func = nn.NodeMap().evaluate
    func = benchmark.Benchmark().f6

    sw = swarm.Swarm(population_size=args.pop, \
                        dimensions=args.d, c1=args.c, c2=args.c)

    pso = swarm.PSO(iter_max=args.iter_max, err_crit=args.err_crit)

    pso.optimize(func, sw)

if __name__ == "__main__":
    main()
