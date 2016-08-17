# deepmap

Implemention of a particle swarm optimized multidimensional neural network (so many syllables!!). 
Nodes (i.e., neurons) are randomly initialized on a plane; node connections are within a 
chosen parameter for maximum distance in Euclidean space. 

## XOR Example
```
$ git clone https://github.com/ReedAnders/deepmap
$ cd deepmap
$ python -m deepmap 
```
```
RESULTS
-------
gbest fitness   :  0.999999999985
gbest params    :  [ -5.46520957   7.44231409  -4.60791218   3.40528773   5.20195263
 -12.8052333    9.21049771  20.36332926  26.2081696    6.47789349
 -20.38761959  14.59293287  -9.98683684  15.51307728 -10.71853549
   7.42635832 -19.23072725  13.85187849  15.75906866  -3.27689558
 -15.17759638  19.53685057   7.6916622   13.81043671 -17.66550159
   4.08678768  18.22758213  -6.46880024  12.07631806  -6.63047308
   2.55083104   8.8045901   -7.99352363  15.76977123  -5.66387318
   7.08445254  -4.34120774  -9.40233211  11.51649327]
iterations      :  961
```
