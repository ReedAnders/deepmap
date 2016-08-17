# Copyright (C) 2016 Reed Anderson.
# From: https://github.com/ReedAnders/deepmap
# License: MIT BY https://opensource.org/licenses/MIT

import pickle, os, binascii
from collections import deque
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

        self.update_input_values()

        # pickle.dump( self.coordinate_map, open( "pickles/coordinate_map.p", "wb" ) )
        # pickle.dump( self.input_nodes, open( "pickles/input_nodes.p", "wb" ) )
        # pickle.dump( self.output_nodes, open( "pickles/output_nodes.p", "wb" ) )
        # pickle.dump( self.latent_nodes, open( "pickles/latent_nodes.p", "wb" ) )

    def calculate_dimensions(self):

        n_params = 0

        for node in self.all_nodes:
            n_params += 2
            n_params += len(node.true_neighbor_index)

        return n_params

    def error(self, correct_labels, predicted_labels):
        error = None
        pattern_error = []
        n_training_patterns = len(correct_labels)

        for i in range(n_training_patterns):

            _sum = sum([(y-o)**2 for y,o in zip(correct_labels, predicted_labels)])
            pattern_error.append(_sum)

        error = 1.0/n_training_patterns * sum(pattern_error)
        return error

    def train(self, training_patterns, param):

        n_training_patterns = len(training_patterns)

        for i in training_patterns:
            n_labels = len(self.output_nodes)
            inputs = i[:-n_labels]

            c_labels = i[-n_labels:]
            p_labels = self.evaluate_topology(inputs, param)

        error = self.error(c_labels, p_labels)
        fitness = 1 - error

        print 'ERROR: %r' % (error)
        return error, fitness

    def evaluate_topology(self, data, param):

        p_labels = []

        # Trim parameters
        p_len = len(param)
        t_len = len(self.latent_nodes + self.output_nodes) * 2
        w_len = p_len - t_len

        w_para = param[:w_len]
        # t_para = deque(param[w_len-2:])

        # Evaluate function
        for node in self.latent_nodes + self.output_nodes:
            self.evaluate_weights(w_para)
            t_para = deque(param[w_len-2:])
            for node in self.latent_nodes + self.output_nodes:
                node_topo_params = [t_para.popleft() for _i in range(2)]
                node.eval_neighbors(node_topo_params[0],node_topo_params[1])

        # Return predicted labels
        p_labels = [node.value for node in self.output_nodes]
        return p_labels

    def evaluate_weights(self, param):
        w_para = deque(param)
        for node in self.latent_nodes + self.output_nodes:
                neighbors = len(node.true_neighbor_index)
                node_weight_params = [w_para.popleft() for _i in range(neighbors)]
                node.eval_sigmoid(node_weight_params)
        self.update_input_values()


    def update_input_values(self):
        for node in self.output_nodes + self.latent_nodes:
            for index in node.true_neighbor_index:
                node.input_values.append(self.all_nodes[index].value)


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

