# Benchmark and Metrics for boundary identification
## Benchmarks
### Introduction
To uniformly and cost-effectively compare adaptive sampling algorithms for boundary identification, we design a series of benchmarks.\
These benchmarks varying in the dimension and range of the input space, the pattern of the boundary, the number of decision modes.

|                                                                     | **Benchmark1** | **Benchmark2**| **Benchmark3**|**Benchmark4**| **Benchmark5** | **Benchmark6**| **Benchmark7**| **Benchmark8**| **Benchmark9** |
|---------------------------------------------------------------------| ------- |---------------------------------|----------------------------------|--------------------------------|----------------------------------|----------------------------------|------------------------------|----------------------------------|----------------|
| range of the input space |only 2 dimension|any dimension|any dimensionn|any dimension|only 2 dimension|only 2 dimension|any dimension|only 2 dimension|any dimension|
| dimension of the input space |[-4,4]<sup>2</sup>|[-10,10]<sup>d</sup>|[-50,50]<sup>d</sup>|[-500,500]<sup>d</sup>| [-10,10]<sup>2</sup>|[-50,50]<sup>2</sup>|[-10,10]<sup>d</sup>| [-20,20]<sup>2</sup>|[-50,50]<sup>d</sup>|
| The lanscapes of Benhmarks <br/>under 2D input and 2 decision modes |![](.\\pictures\\Benchmark1.jpg) | ![](.\\pictures\\Benchmark2.jpg) | ![](.\\pictures\\Benchmark3.jpg) | ![](.\\pictures\\Benchmark4.jpg) | ![](.\\pictures\\Benchmark5.jpg) | ![](.\\pictures\\Benchmark6.jpg) | ![](.\\pictures\\Benchmark7.jpg) | ![](.\\pictures\\Benchmark8.jpg) |![](.\\pictures\\Benchmark9.jpg)



### Usage
Boundary_benchmark.py integrates 9 Benchmarks.\
The true boundary points folder contains the true boundary points files for 2D and 3D Benchmarks under 2 and 4 decision modes.

---
## Metrics
The purpose of the adaptive sampling methods for boundary identification is to cover as full boundary as possible with fewer sample points.
Considering the overall evaluation of the sampling performance, we propose four evaluation metrics.\
In the following formula, *TB* and *b<sub>i</sub>* represent the set of true boundary points and one of the true boundary points.\
*S* and *s<sub>i</sub>* represent the set of sample points and one of the sample points.\
*D<sub>$\lambda$</sub>* represents the width of the boundary regions. 

*  **Coverage**\
The coverage metric measures the diversity of sampling, denoting the percentage of the true boundary points that have beeb sampled:\
![](.\\pictures\\cov.png)


* **Precision**\
The precision metric is the percentage of sample points within true boundary regions.\
![](.\\pictures\\pre.png)

* **Efficiency**\
The efficiency metric is the percentage of sample points within true boundary regions to the query number of the actual system.\
![](.\\pictures\\eff.png)
