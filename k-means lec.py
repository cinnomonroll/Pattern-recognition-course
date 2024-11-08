C1, C2

consistency = [0 x in range(10)]
for i in range():
	label of the data point in the cluster
	consistency[label]+=1
	
max(consistency)/sum(consistency)


def cosine_dist(x,z):
	return dist(x,z)
    
def calc_error(prev_centroids, new_centroids):
    for i in range(len(new_centroids)):
        err += cosine_dist(prev_centroids[i],new_centroids[i])
    return err

X = []
y_cluster = []
k = 2
epsilon = 0.00001

centroids = X[0:k]

err = 10
i = 0
while (err>epsilon or i<100):
    prev_centroids = centroids
    # assign data points to their closest centroids
    
    # recalcualte centroids 
    
    err = calc_error(prev_centroids, centroids)
    
    i+=1
