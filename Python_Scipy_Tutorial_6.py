# Working with spatial data: it refers to data thzt is represented in a geometric space.
# Triangulation: one method to generate these triangulation through the point is delaunay() triangulation.

# here now we will create a triangualtion from some points:
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

bhupeshwar_3d = np.array([[2,4], [3,4], [3,0], [2,2], [4,1]])
simplices = Delaunay(bhupeshwar_3d).simplices
plt.triplot(bhupeshwar_3d[:,0], bhupeshwar_3d[:,1], simplices)
plt.scatter(bhupeshwar_3d[:,0], bhupeshwar_3d[:,1], color='r')
plt.show()


# Convex HUll: it is the smallest polygon that covers all of the given point:

import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

bhupeshwar_3d = np.array([[2,4], [3,4], [3,0], [2,2], [4,1], [1,2], [5,0], [3,1],[1,2],[0,2]])

hull = ConvexHull(bhupeshwar_3d)
hull_points = hull.simplices
plt.scatter(bhupeshwar_3d[:,0], bhupeshwar_3d[:,1])
for simplex in hull_points:
    plt.plot(bhupeshwar_3d[simplex,0], bhupeshwar_3d[simplex,1], 'k-')
plt.show()

# KDTrees: they are a data structures optimized for the nearest neighbour queries.
from scipy.spatial import KDTree
bhupeshwar_2d = [(1,-1), (2,3), (-2,3), (2,-3)]
tree = KDTree(bhupeshwar_2d)
res = tree.query((1,1))
print(res)


# Distance matrix: it is used to find the various types of distance between 2 points . there are basically 2 types: Euclidean Distance, Cosine Distance.
# Euclidean Distance: 
from scipy.spatial.distance import euclidean
p1 = (1,0)
p2 = (10,2)
bhupeshwar = euclidean(p1, p2)
print(bhupeshwar)

# Cosine Distance: 
from scipy.spatial.distance import cosine
p1 = (1,0)
p2 = (10,2)
bhupeshwar = cosine(p1, p2)
print(bhupeshwar)