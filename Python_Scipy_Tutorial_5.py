# working with graphs: we have a module named scipy.sparse.csgraph
# adjacency Matrix: nxn matrix where n is the number of element in the graph.
# Connected Component:

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

bhupeshwar_2d = np.array([[0,1,2], [1,0,0], [2,0,0]])
bhupeshwar_new = csr_matrix(bhupeshwar_2d)
print(connected_components(bhupeshwar_new))


# Dijkstra method: for finding the shortest path in a graph from one element to another
# it take 3 arg: return_predecessors, indices, limit
# here we will find te shortest path from element 1 to 2:

import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

bhupeshwar_2d = np.array([[0,1,2], [1,0,0], [2,0,0]])
bhupeshwar_new = csr_matrix(bhupeshwar_2d)
print(dijkstra(bhupeshwar_new, return_predecessors=True, indices=0))


# Floyd Warshall() method: it is for finding the shortest path between all the pairs of elements.

import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

bhupeshwar_2d = np.array([[0,1,2], [1,0,0], [2,0,0]])
bhupeshwar_new = csr_matrix(bhupeshwar_2d)
print(floyd_warshall(bhupeshwar_new, return_predecessors=True))


# Bellman_ford() method: it is for finding the shortest path between all the pairs of elements but this method can handle negative weight as well:


import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

bhupeshwar_2d = np.array([[0,-1,2], [1,0,0], [2,0,0]])
bhupeshwar_new = csr_matrix(bhupeshwar_2d)
print(bellman_ford(bhupeshwar_new, return_predecessors=True, indices=0))

# Depth first order: it returns a depth first traversal froma node: it has 2 argu: the graph, starting element

import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix
bhupeshwar_2d = np.array([[0,1,0,1], [1,1,1,1], [2,1,1,0],[0,1,0,1]])
bhupeshwar_new = csr_matrix(bhupeshwar_2d)
print(depth_first_order(bhupeshwar_new, 1))


# breadth_first_order() method: it returns the breadth from a node:it has 2 argu: the graph, starting element

import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix
bhupeshwar_2d = np.array([[0,1,0,1], [1,1,1,1], [2,1,1,0],[0,1,0,1]])
bhupeshwar_new = csr_matrix(bhupeshwar_2d)
print(breadth_first_order(bhupeshwar_new, 1))