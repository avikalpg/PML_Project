#!/usr/bin/python

#############################
# This is the newer version #
# of the data generator:	#
# It uses multivariant gaus #
#############################

import numpy as np
import pickle

numClasses = 6
numDim = 2
ease = 10 		# keep this 4
# Limits on the number of data points in a single class
lowerLim = 50
upperLim = 1000

def generate(numClasses, dim):
	data = np.empty(shape=[0, 2])
	mus = []
	sigmas = []
	for x in xrange(numClasses):
		mu = ease * (np.random.rand(dim) - 0.5)
		sigma = 4 * (np.random.rand(dim, dim) - 0.5)
		sigma = np.dot(sigma.T, sigma)
		size = np.random.randint(50, 1000)
		local = np.random.multivariate_normal(mu, sigma, size)
		# print np.shape(local)
		# local = local.T
		local = np.array([(row, x) for row in local])
		data = np.append(data, local, axis=0)
		# print np.shape(local), local
		mus.append(mu)
		sigmas.append(sigma)
	return (data, mus, sigmas)

data = generate(numClasses, numDim)
with open("pickle/data_k"+str(numClasses)+"_dim"+str(numDim)+"_ease"+str(ease)+".pickle", 'wb') as f:
	pickle.dump(data, f)

# print data[0]
# print np.shape(data[0])
