#!/usr/bin/python

#############################
# this is the older version #
#############################

import numpy as np
import pickle

numClasses = 6
numDim = 2
# numSamples = 100
numSamples = 'variable'
ease = 10 		# keep this 4

def generate(numClasses, dim, size):
	data = np.empty(shape=[0, 2])
	mus = []
	sigmas = []
	flag = False
	if size == 'variable':
		flag = True
	for x in xrange(numClasses):
		mu = []
		sigma = []
		if flag :
			size = np.random.randint(50, 1000)
		local = np.empty(shape=[0,size])
		for i in xrange(dim):
			mu.append(ease * (np.random.rand() - 0.5))
			sigma.append(2 * np.random.rand() + 0.2)
			localDim = np.random.normal(mu[-1], sigma[-1], size)
			# print np.shape(local), np.shape(localDim)
			local = np.append(local, localDim.reshape(1,size), axis=0)
			# print local
		# print local.T
		local = local.T
		local = np.array([(row, x) for row in local])
		data = np.append(data, local, axis=0)
		# print np.shape(local), local
		mus.append(mu)
		sigmas.append(sigma)
	return (data, mus, sigmas)

data = generate(numClasses, numDim, numSamples)
with open("pickle/data_k"+str(numClasses)+"_dim"+str(numDim)+"_size"+str(numSamples)+"_ease"+str(ease)+".pickle", 'wb') as f:
	pickle.dump(data, f)

# print data
# print np.shape(data)
