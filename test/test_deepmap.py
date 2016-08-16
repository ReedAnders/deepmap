import unittest
import numpy as np
from deepmap import swarm, nn

class TestStringMethods(unittest.TestCase):

    def test_swarm(self):
        sw = swarm.Swarm()
        self.assertEqual(120, len(sw.population))
        self.assertEqual(type(0.0), type(sw.c1))

    def test_particle(self):
        p = swarm.Particle(10)
        self.assertEqual(p.params[0], p.pBest[0])
        self.assertEqual(p.dimensions, 10)

    def test_nn(self):
        n1 = nn.NodeMap(input_node_population=12, output_node_population=1, \
            latent_node_population=400)
        self.assertEqual(n1.all_nodes[0].name,n1.input_nodes[0].name)
        self.assertEqual(n1.all_nodes[-1].name,n1.latent_nodes[-1].name)

    def test_nn_constructor(self):
        n1 = nn.NodeMap(input_node_population=12, output_node_population=1, \
            latent_node_population=400)
        n1.construct_map()

        def mutual_nodes(position):
            node_1 = n1.all_nodes[position]
            node_2 = []
            contains = False

            for neighbor in node_1.neighbors:
                if neighbor[1] == True:
                    node_2.append(neighbor[0][0])

            # print node_2
            for index in node_2:
                for node in n1.all_nodes:
                    if node.name == index:
                        for neighbor in node.neighbors:
                            if neighbor[1] == True and \
                             neighbor[0][0] == node_1.name:
                                contains = True
                                break

            return contains

        i = 0
        while i < 2000:
            position = np.random.randint(len(n1.all_nodes)-1)
            r1 = mutual_nodes(position)
            self.assertTrue(r1)
            i += 1

    def test_nn_error(self):
        n1 = nn.NodeMap()
        c_labels = [0,1,0,1]
        p_labels = [0,1,0,0]

        self.assertEqual(n1.error(c_labels, p_labels),1)

        p_labels = [0,1,0,1]
        self.assertEqual(n1.error(c_labels, p_labels),0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
