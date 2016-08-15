import numpy as np
from math import exp
from random import random

class NodeMap:
    def __init__(self, input_node_population=12, output_node_population=1, latent_node_population=4000):
        self.coordinate_map = []
        self.input_nodes = [InputNode() for node in range(input_node_population)]
        self.output_nodes = [Node() for node in range(output_node_population)]
        self.latent_nodes = [Node() for node in range(latent_node_population)]

    # def __repr__(self):
    #     return 'NodeMap(input_nodes=%r, output_nodes=%r, latent_nodes=%r)' \
    #             % (self.input_node_population, self.output_node_population, \
    #                 self.latent_node_population)

    def construct_map(self):
        for node in self.input_nodes + self.output_nodes + self.latent_nodes:
            self.coordinate_map.append(node.coordinates)

        for node in self.input_nodes + self.output_nodes + self.latent_nodes:
            node.find_neighbors(self.coordinate_map)

    def evaluate(self, param):

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
        self.coordinates = np.array([random() for i in range(dimensions)])
        self.value = 0.0
        self.neighbors = []

    def __repr__(self):
        return 'Node(%r, value=%r, neighbors=%r)' % (self.coordinates, \
            self.value, self.neighbors)

    def find_neighbors(self, coordinate_map):
        for node in coordinate_map:
            result = 1 if np.linalg.norm(self.coordinates-node) < 0.1 else 0
            self.neighbors.append(result)

class InputNode(Node):
    def __init__(self):
        Node.__init__(self)

    def __repr__(self):
        return 'Node(%r, value=%r, neighbors=%r)' % (self.coordinates, \
            self.value, self.neighbors)


