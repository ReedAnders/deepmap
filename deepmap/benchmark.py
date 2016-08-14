from math import sin, sqrt

class Benchmark:
    def __init__(self):
        pass

    def f6(self, param):
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
