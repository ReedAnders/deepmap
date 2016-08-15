import numpy as np
from math import exp
from random import random

class NNetwork:
    def __init__(self):
        self.input_nodes = [Node() for node in range(input_node_population)]
        self.output_nodes = [Node() for node in range(output_node_population)]
        self.latent_nodes = [Node() for node in range(latent_node_population)]

    def testNN(self, param):

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
