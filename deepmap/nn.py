# Copyright (C) 2016 Reed Anderson.
# From: https://github.com/ReedAnders/deepmap
# License: MIT BY https://opensource.org/licenses/MIT

import pickle, os, binascii
import numpy as np
from math import exp
from random import random

class NodeMap:
    def __init__(self, input_node_population=12, output_node_population=1, latent_node_population=400):
        self.coordinate_map = []
        self.input_nodes = [Node() for node in range(input_node_population)]
        self.output_nodes = [Node() for node in range(output_node_population)]
        self.latent_nodes = [Node() for node in range(latent_node_population)]
        self.all_nodes = self.input_nodes + self.output_nodes + self.latent_nodes


    def construct_map(self):
        for node in self.all_nodes:
            self.coordinate_map.append((node.name, node.coordinates))

        for node in self.all_nodes:
            node.find_neighbors(self.coordinate_map)

        # pickle.dump( self.coordinate_map, open( "pickles/coordinate_map.p", "wb" ) )
        # pickle.dump( self.input_nodes, open( "pickles/input_nodes.p", "wb" ) )
        # pickle.dump( self.output_nodes, open( "pickles/output_nodes.p", "wb" ) )
        # pickle.dump( self.latent_nodes, open( "pickles/latent_nodes.p", "wb" ) )


    def evaluate_topology(self, param):

        # Trim parameters
        para = param[0:2]

        # Evaluate function
        num = (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) * \
            (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) - 0.5
        denom = (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1]))) * \
                (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1])))
        f6 =  0.5 - (num/denom)

        # Calculate error
        errorf6 = 1 - f6

        # Return solution and error
        return f6, errorf6

    def evaluate_weights(self, param):

        # Trim parameters
        para = param[0:2]

        # Evaluate function
        num = (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) * \
            (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) - 0.5
        denom = (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1]))) * \
                (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1])))
        f6 =  0.5 - (num/denom)

        # Calculate error
        errorf6 = 1 - f6

        # Return solution and error
        return f6, errorf6


class Node:
    def __init__(self, dimensions=3):
        self.name = binascii.b2a_hex(os.urandom(8))
        self.coordinates = np.array([random() for i in range(dimensions)])
        self.value = 0.0
        self.neighbors = []

    def __repr__(self):
        return 'Node(%r, value=%r, neighbors=%r)' % (self.coordinates, \
            self.value, self.neighbors)

    def find_neighbors(self, coordinate_map):
        for node in coordinate_map:
            result = 1 if np.linalg.norm(self.coordinates-node[1]) < 0.1 else 0
            self.neighbors.append((node[0],result))


