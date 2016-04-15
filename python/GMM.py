#!/usr/bin/python

import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as gauss

numClasses = 6
numDim = 2
# numSamples = 100
numSamples = 'variable'
ease = 10

sym_map = {0:'r.', 1:'b.', 2:'y.', 3:'g.', 4:'c.', 5:'m.', 6:'k.', 7:'w.', 8:'r-', 9:'b-', 10:'g-', 11:'y^', 12:'r^', 13:'b^', 14:'g^', 14:'rx', 15:'bx', 16:'gx', 17:'yx', 18:'g^'}

def plot_data(data):
	x_vals = []
	y_vals = []
	label = 0
	args = []
	classSizes = {}
	for point in data:

		classSizes[point[1]] = classSizes.get(point[1], 0) + 1
		colorVar = float(point[1])/float(numClasses)

		if label == point[1]:
			x_vals.append(point[0][0])
			y_vals.append(point[0][1])
		else:
			args.append(x_vals)
			args.append(y_vals)
			# args.append(sym_map[label])
			args.append('1')
			# args.append('marker=\'.\'')
			# args.append('linewidth=0')
			label += 1
			x_vals = [point[0][0]]
			y_vals = [point[0][1]]
	args.append(x_vals)
	args.append(y_vals)
	args.append(sym_map[label])
	# plt.plot(x_vals, y_vals, color=(0, float(label)/float(numClasses), 0, 1), marker='.', linewidth=0)
	print classSizes

	plt.plot(*args)
	plt.show()

def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)

def GMM(data, k, dim):
	# Initializing pi, mu and Sigma
	pi = [1.0/k]*k
	mu = []
	sigma = []
	N = len(data)
	for x in xrange(k):
		mu.append(ease * (np.random.rand(dim) - 0.5))
		cov = 4 * (np.random.rand(dim, dim) - 0.5)
		cov = np.dot(cov.T, cov)
		sigma.append(cov)

	while True:
		# Estimating Expectation
		gamma = np.empty(shape=[0, N])
		for x in xrange(k):
			# print sigma[x]
			Normal= gauss(mean=mu[x], cov=sigma[x])
			N_n = pi[x] * Normal.pdf(data)
			gamma = np.append(gamma, N_n.reshape(1, N), axis=0)
		print "Shape of the gamma:", np.shape(gamma)
		for x in xrange(np.shape(gamma)[1]):
			# print gamma[:,x],
			gamma[:,x] = gamma[:,x] / np.sum(gamma[:,x])
			# print gamma[:,x]

		# Maximizing Expectation
		mu = np.dot(gamma, data)
		for x in xrange(k):
			N_k = np.sum(mu[x])
			mu[x] = mu[x] / N_k
			pi[x] = N_k / N

			cov = data - [mu[x]]*N
			for i in xrange(len(cov)):
				dummy = np.multiply(np.outer(cov[i], cov[i]), gamma[x][i])
				if not is_pos_def(dummy):
					print "BETA: One of the included matrices is not positive definite!!!"
			# cov = np.array([np.multiply(np.outer(cov[i], cov[i]), gamma[x][i]) for i in xrange(len(cov))])
			cov = np.sum([np.multiply(np.outer(cov[i], cov[i]), gamma[x][i]) for i in xrange(len(cov))], axis=0)
			# print cov, np.shape(cov)
			if not is_pos_def(cov):
				print "BETA: This is not positive definite!!!"
			sigma[x] = cov
		print "Shape of sigma", np.shape(sigma)
		# Checking Convergence
		# break

def main():
	print "Loading the data",
	# with open("pickle/data_k"+str(numClasses)+"_dim"+str(numDim)+"_size"+str(numSamples)+"_ease"+str(ease)+".pickle", 'rb') as f:
	# 	data, means, covariances = pickle.load(f)
	with open("pickle/data_k"+str(numClasses)+"_dim"+str(numDim)+"_ease"+str(ease)+".pickle", 'rb') as f:
		data, means, covariances = pickle.load(f)
	print "\rData has been loaded."

	# print np.shape(data)
	# print np.shape(data[0][0])
	# plot_data(data)
	# print data

	points = np.array([point[0] for point in data])
	print "shape of x:", np.shape(points)
	result = GMM(points, numClasses, numDim)

main()