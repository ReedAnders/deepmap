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
        self.input_nodes = [InputNode() for node in range(input_node_population)]
        self.output_nodes = [OutputNode() for node in range(output_node_population)]
        self.latent_nodes = [LatentNode() for node in range(latent_node_population)]
        self.all_nodes = self.input_nodes + self.output_nodes + self.latent_nodes


    def construct_map(self):
        for node in self.all_nodes:
            self.coordinate_map.append((node.name, node.coordinates))

        for node in self.all_nodes:
            node.find_neighbors(self.coordinate_map)

        for node in self.output_nodes + self.latent_nodes:
            for index in node.true_neighbor_index:
                node.input_values.append(self.all_nodes[index].value)

        # pickle.dump( self.coordinate_map, open( "pickles/coordinate_map.p", "wb" ) )
        # pickle.dump( self.input_nodes, open( "pickles/input_nodes.p", "wb" ) )
        # pickle.dump( self.output_nodes, open( "pickles/output_nodes.p", "wb" ) )
        # pickle.dump( self.latent_nodes, open( "pickles/latent_nodes.p", "wb" ) )


    def evaluate(self, param, training_patterns):
        error = None
        pattern_error = None
        n_training_patterns = float(len(training_patterns))

        # i = [float,float,float,float,float,float,float, .. , label]
        for i in training_patterns:
            n_labels = len(self.output_nodes)
            inputs = i[-n_labels:]

            correct_labels = i[:-n_labels]
            predicted_labels = predict(inputs)

            pattern_error = sum([(y-o)**2 for y,o in \
                zip(correct_labels, predicted_labels)])

        error = 1/n_training_patterns * sum(pattern_error)


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


        # Evaluate function


        # Calculate error
        errorf6 = 1 - f6

        # Return solution and error
        return f6, errorf6


class Node:
    def __init__(self, dimensions=3):
        self.name = binascii.b2a_hex(os.urandom(8))
        self.coordinates = np.array([random() for i in range(dimensions)])
        self.neighbors = []
        self.true_neighbor_index = []
        self.optimal_neighbor_set = set()
        self.value = 0.0

    def find_neighbors(self, coordinate_map):
        for index, node in enumerate(coordinate_map):
            if np.linalg.norm(self.coordinates-node[1]) < 0.1:
                self.true_neighbor_index.append(index)
                self.neighbors.append((node,True))
            else:
                self.neighbors.append((node,False))

    # Two parameters between -1, 1
    def eval_neighbors(self, lower_bound, upper_bound):
        for index in self.true_neighbor_index:
            dist = np.linalg.norm(self.coordinates-self.neighbors[index][0][1])
            if dist > lower_bound and dist < upper_bound:
                self.optimal_neighbor_set.add(index)

class InputNode(Node):
    def __init__(self):
        Node.__init__(self)

class LatentNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.value = random()
        self.input_values = []

    # Multiple parameters for n weights -1, 1
    def eval_sigmoid(self, weights):
        x = sum([w*v for w,v in zip(weights, self.input_values)])
        self.value = 1 / (1 + exp(-x))

class OutputNode(LatentNode):
    def __init__(self):
        LatentNode.__init__(self)

