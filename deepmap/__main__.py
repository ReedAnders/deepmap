# Copyright (C) 2016 Reed Anderson.
# From: https://github.com/ReedAnders/deepmap
# License: MIT BY https://opensource.org/licenses/MIT

from random import random
import argparse
import csv

import swarm
import benchmark
import nn

def main():

    parser = argparse.ArgumentParser(description='Run PSO on a benchmark')
    parser.add_argument('--pop', default=120, type=int,
                        help='swarm population size')
    # parser.add_argument('--d', default=2, type=int,
    #                     help='solution dimension size')
    parser.add_argument('--c', default=2.0, type=float,
                        help='particle acceration constant')
    parser.add_argument('--err_crit', default=0.0000000001, type=float,
                        help='error criteria for stopping PSO')
    parser.add_argument('--iter_max', default=10000, type=float,
                        help='maximum iterations for stopping PSO')
    parser.add_argument('--data', required=True, type=str,
                        help='required data csv')
    args = parser.parse_args()


    data = []
    with open(args.data,'rb') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            if index == 0:
                continue
            row = [float(i) for i in row]
            data.append(row)

    input_nodes = 2

    # func = nn.NodeMap().evaluate
    # func = benchmark.Benchmark().f6
    n1 = nn.NodeMap(input_node_population=input_nodes, latent_node_population=10)
    n1.construct_map()

    d = n1.calculate_dimensions()

    func = n1.train

    sw = swarm.Swarm(population_size=args.pop, \
                        dimensions=d, c1=args.c, c2=args.c)

    pso = swarm.PSO(iter_max=args.iter_max, err_crit=args.err_crit)

    pso.optimize(func, sw, data)

if __name__ == "__main__":
    main()
