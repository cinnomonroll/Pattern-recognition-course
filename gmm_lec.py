import numpy as np


def estimate_cluster_parameters(X, r_k):
    # Compute the updated parameters for each cluster
    n, d = X.shape
    mu = np.sum(r_k[:, np.newaxis] * X, axis=0) / np.sum(r_k)
    sigma = np.sum(r_k[:, np.newaxis] * (X - mu) ** 2, axis=0) / np.sum(r_k) - mu ** 2
    pi = np.sum(r_k) / n
    return mu, sigma, pi

    
def estimate_r_k (cluster_parameter):
    #implement the formula for r_k_i
    return r_k
# class cluster_parameters:
#     def __init__():
#         mu = 
#         sigma = 
#         pi = 

class cluster_parameters:
    def __init__(self, K, d):
        # Initialize parameters for K clusters
        self.mu = []  # List of mean vectors (each of dimension d)
        self.sigma = []  # List of diagonal covariance vectors (each of dimension d)
        self.pi = []  # List of mixing coefficients (one for each cluster)

        # Initialize each parameter for K clusters
        for _ in range(K):
            self.mu.append([0.0] * d)  # Initialize mean vector with zeros
            self.sigma.append([1.0] * d)  # Initialize diagonal covariance vector with ones
            self.pi.append(1.0 / K)  # Initialize equal mixing coefficients


def GMM(X, k, epoch=100):
    n, d = X.shape  # Number of data points and features
    cluster_assignments = np.zeros((n,))
    cluster_parameters_k = [cluster_parameters(d) for _ in range(k)]  # Initialize parameters for K clusters
    r_k_clusters = np.ones((n, k))


# def GMM(X,k,epoch=100):
#     cluster_assignments = np.zeros((len(X),))
#     cluster_prameters_k = [cluster_assignments(),cluster_assignments(),..,] # size k, each value is class_parameter object
#     r_k_clusters = np.ones((k,))    #note that this is only for one image/data point only. You need a matrix for all data points and all clusters
    for i in range(len(X)):
        cluster_assignments[i] = #random number between 1 to k
    for i in range(k):
        index = np.where(cluster_assignments==i)
        mu, sigma, pi = estimate_cluster_parameters(X[index],r_k_clusters)
        cluster_prameters_k[i].sigma = sigma
        # same for mu and pi
    i = 0
    while (i<epoch):
        # E step 
        for j in range(k):
            r_k_clusters[j] = estimate_r_k(cluster_prameters_k[i])
        # M Step
        for j in range(k):
            index = np.where(cluster_assignments==i)
            mu, sigma, pi = estimate_cluster_parameters(X[index],r_k_clusters)
            cluster_prameters_k[i].sigma = sigma
    