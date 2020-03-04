import scipy.stats as ss
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def simulate_data(N,mu,sigma2):
	x = np.random.multivariate_normal(mean=mu, cov=sigma2, size=N)
	return x

def plot_points(x,y,):
	plt.scatter(x,y)

def EM(dat,K,eps):
	X = np.array(dat)
	N, d = X.shape
	mu, sigma2, pi = initialize(X,K)
	lold = -1000
	lnew = -999
	while(np.abs(lnew - lold > eps)):
		Z = Estep(X, mu, sigma2, pi)
		mu, sigma2, pi = Mstep(X, Z)
		lold = lnew
		lnew = logLikelihood(X, mu, sigma2, pi, Z)
		print(lold,lnew)
	return membership(Z), lnew

def initialize(X,K):
	N, d = X.shape
	mu = np.mean(X,0)
	sigma2 = np.cov(X.T)
	mu_clusters = np.random.multivariate_normal(mu, sigma2, K)
	sigma2_clusters = np.tile(sigma2,(K,1,1)) + np.abs( np.random.normal(0,1,(K,1,1)) )
	pi_clusters = np.random.uniform(0,1,K)
	pi_clusters = pi_clusters / pi_clusters.sum()

	return mu_clusters, sigma2_clusters, pi_clusters

def Estep(X, mu, sigma2, pi):
	N = X.shape[0]
	K = pi.shape[0]
	Z = np.zeros( (N,K) )
	PGauss = np.zeros( (N,K) )
	for i in range(N):
		for k in range(K):
			PGauss[i,k] = ss.multivariate_normal.pdf(X[i],mean=mu[k],cov=sigma2[k])
		denominator = np.dot(PGauss[i,:],pi)
		for k in range(K):
			Z[i,k] = PGauss[i,k]*pi[k] / denominator
	return Z


def Mstep(X, Z):
	N, d = X.shape
	K = Z.shape[1]
	mu_clusters = np.zeros((K,d))
	sigma2_clusters = np.zeros((K,d,d))
	pi_clusters = np.zeros( K )
	
	pi_clusters = np.sum(Z,0) / N

	mu_clusters = np.sum( np.transpose( np.expand_dims(X,2)*np.expand_dims(Z,1), [2,0,1] ), 1 )
	mu_clusters = mu_clusters / np.expand_dims( pi_clusters*N, 1)

	sigma2_clusters = np.expand_dims(X,0) - np.expand_dims(mu_clusters,1)
	sigma2_clusters = np.expand_dims(sigma2_clusters,2) * np.expand_dims(sigma2_clusters,3)
	sigma2_clusters = np.sum( np.transpose(Z,[1,0])[...,np.newaxis,np.newaxis]*sigma2_clusters,1)
	sigma2_clusters = sigma2_clusters / np.sum(Z,0)[...,np.newaxis,np.newaxis]

	return mu_clusters, sigma2_clusters, pi_clusters


def logLikelihood(X, mu, sigma2, pi, Z):
	N, d = X.shape
	K = Z.shape[1]
	PGauss = np.ones((N,K))
	for i in range(N):
		for k in range(K):
			PGauss[i,k] = ss.multivariate_normal.pdf(X[i],mean=mu[k],cov=sigma2[k])
	return np.log(np.matmul(PGauss,pi)).sum()

def membership(Z):
	return np.argmax(Z,1)


if __name__ == "__main__":
	N = 20
	mu = [1,2]
	sigma2 = [[1,0],[0,0.1]]
	dat1  = simulate_data(N,mu,sigma2)
	dat = dat1[:]

	N = 30
	mu = [3,4]
	sigma2 = [[1,0],[0,0.1]]
	dat2  = simulate_data(N,mu,sigma2)
	dat = np.append(dat,dat2,axis=0)

	v_group = np.append( np.zeros(20),np.ones(30) )
	print(v_group)

	K = 2
	eps = 0.1
	#Z =  Estep(dat, *initialize(dat,K))
	#print("Z:")
	#print(Z)
	#print("mu, sigma2, pi")
	#mu, sigma2, pi = Mstep(dat,Z)
	#print(mu)
	#print(sigma2)
	#print(pi)
	#print( logLikelihood(dat, mu, sigma2, pi, Z) )
	grp, l =  EM(dat,K,eps)
	print(grp.tolist())

	#plot_points(dat1[:,0],dat1[:,1])
	#plot_points(dat2[:,0],dat2[:,1])
	colors = ['red' if i==0 else 'blue' for i in v_group]
	labels = ['+' if i == 0 else '*' for i in grp]

	plt.scatter(dat[:,0], dat[:,1], c=colors, s=(grp+0.1)*100 )
	plt.show()








