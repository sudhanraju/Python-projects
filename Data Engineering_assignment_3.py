
# coding: utf-8

# In[11]:


from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# In[44]:


#data preparation
iris = datasets.load_iris()

x=iris.data
y=iris.target

# Part 1 of Assigment 7 
#Kmeans
from sklearn.cluster import KMeans
clustering = KMeans(n_clusters=3)
y_pred = clustering.fit_predict(x)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x[:,0], x[:,1], x[:,2], c=y_pred)
plt.show()

#Hierarchical - Agglomerative Clustering
from sklearn.cluster import AgglomerativeClustering

model = AgglomerativeClustering(n_clusters=3, linkage="ward")
y_pred = model.fit_predict(x)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x[:,0], x[:,1], x[:,2], c=y_pred)
plt.show()


# Running it using 2 predictors 

full_data = np.empty((150,3), dtype='float32')
for i in range(150):
    full_data[i,0] = x[i,0]
    full_data[i,1] = x[i,0]
    full_data[i,2] = y[i]
    
np.random.shuffle(full_data)

training_data = full_data[:130,:]
testing_data = full_data[130:,:]

model = KMeans()
model.fit(training_data[:,:2], training_data[:,2])

test_results = np.array([model.predict(i[:2].reshape(1,-1)) for i in testing_data], dtype='float32')

correct = 0 

for idx, _ in enumerate(test_results):
    if test_results[idx] == testing_data[idx,2]:
        correct += 1

print('model Accuracy:\t{}'.format(correct /len(test_results)))
plt.scatter(x[:,0],x[:,1], c=y)
plt.show()

test_results = np.array([model.predict(i[:2].reshape(1,-1)) for i in full_data], dtype='float32')
plt.scatter(x[:,0],x[:,1], c=y)
plt.show()



# In[46]:


#part 2 of Assigment 7 
#Using the provided y values as “ground truth”, calculate the adjusted rand index
#Using the provided y values as “ground truth”, calculate the adjusted rand index.
# 1. Does the selection of predictors have an effect on the ARI?

iris = datasets.load_iris()

x=iris.data
y=iris.target

from sklearn import metrics

ground_truth = y
predicts = y_pred
print(metrics.adjusted_rand_score(ground_truth,predicts))


# In[47]:


# part 3 
# Yes, selection of predictors have effect. 


# In[48]:


#part 4 -  Repeat this analysis using c-means fuzzy clustering. Which clustering performs better in this case, fuzzy
# or traditional clustering


# Answer - Sorry. I dont understand c-means fuzzy clustering. I was going through the recording again 
#but i wasnt sure at all. 

