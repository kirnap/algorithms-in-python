# This code is for fully educational purposes and it implements the simulated annealing AI algorithm
# for more information please visit: https://en.wikipedia.org/wiki/Simulated_annealing



import numpy
import time
import random


NEIGHBORHOOD_MAX = 40
NEIGHBORHOOD_MIN = 0
T_MAX = 100
T_MIN = 0.01



def f(x):
	assert NEIGHBORHOOD_MIN <= x <= NEIGHBORHOOD_MAX
	return numpy.sin(0.15 * x) + numpy.cos(x)


def acceptance(s, new_s, temperature):
	return numpy.exp(-1 * float(new_s - s) / float(temperature))


def next_neighbor(sol, alpha, T, T_max):
	move = alpha * NEIGHBORHOOD_MAX

	if sol - move <= NEIGHBORHOOD_MIN:
		return sol + move
	elif sol + move >= NEIGHBORHOOD_MAX:
		return sol - move
	else:
		return sol + move * random.uniform(-1, 1)


def SA(sol):
	s = sol
	T = T_MAX

	alpha = 0.4
	beta = 0.9

	while T > T_MIN:
		print 'S: %s | T: %s' % (str(s), str(T))
		for _ in range(200):
			new_s = next_neighbor(s, alpha, T, T_MAX)

			if f(new_s) > f(s) or acceptance(s, new_s, T) > random.uniform(0, 1):
				s = new_s

		alpha *= beta
		T *= beta

	return s, f(s), f(12.6025895306)



if __name__ == '__main__':
	print 'SOL: %s | RESULT: %s | TARGET: %s' % SA(15.0)


	
