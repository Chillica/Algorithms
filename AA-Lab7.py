from functools import lru_cache, reduce
from collections import namedtuple
from collections import defaultdict
SubProb = namedtuple('SubProb', ['value', 'partial', 'args'])


def knapval_rep(capacity, items):
    """returns the maximum value achievable in `capacity`
    weight using `items` when repeated items are allowed"""

    # define and index all subproblems
    @lru_cache(maxsize=None)
    def knapv(w):
        subprobs = [(knapv(w-item.weight) + item.value)
            for item in items if item.weight <= w]
        return reduce(max, subprobs, 0)

    return knapv(capacity)


def knapval_norep_orig(capacity, items):
    """returns the maximum value achievable in `capacity`
    weight using `items` when repeated items are not allowed"""

    @lru_cache(maxsize=None)
    def knapval(w, k):
        """returns max knapsack value with capacity of w choosing from first k items"""
        if k < 1:
            return 0
        # option 1) skip the last item
        options = [knapval(w, k-1)]
        # option 2) take the last item
        last_item = items[k-1]
        if last_item.weight <= w:
            options.append(last_item.value + knapval(w-last_item.weight, k-1))
        # return the best value
        return max(options)
    # the original problem is w is full capacity looking at all items
    return knapval(capacity, len(items))

# for edit_distance,
# rather than conditionally appending applicable sub problems to a list
# I'm going to use a paradigm described in https://stackoverflow.com/a/54939821/3780389
# I find it easier to describe the options that are available
# along with any conditions
Skip = object()
def drop_skipped(itr):
    return filter(lambda v: v is not Skip, itr)

# for example, here is how we might have used this
# idea with knapval_norep:
def knapval_norep(capacity, items):
    """returns the maximum value achievable in `capacity`
    weight using `items` when repeated items are not allowed"""

    @lru_cache(maxsize=None)
    def knapval(w, k):
        """returns max knapsack value with capacity of w choosing from first k items"""
        if k <= 0 or w <= 0:
            return 0
        options = drop_skipped([
            # skip the last item and then do your best
            knapval(w, k-1),
            # take the last item if it fits and then do your best
            items[k-1].value + knapval(w-items[k-1].weight, k-1) if items[k-1].weight <= w else Skip,
        ])
        # return the best value
        return max(options)
    # the original problem is w is full capacity looking at all items
    return knapval(capacity, len(items))

def edit_distance(s1, s2):
    """returns cost of the cheapest alignment between s1 and s2"""
    # define the sub problems in terms of prefix lengths
    @lru_cache(maxsize=None)
    def ed(i, j):
        """cost of aligning first i characters of s1 with first j
        characters of s2"""
        # in following comments, we will refer to p1 and p2 as
        # the prefixes to be aligned by this subproblem. i.e.:
        # p1 = s1[:i] # the first i chars of s1
        # p2 = s2[:j] # the first j chars of s2

        # one approach to the recursive definition is to list out
        # all of the options available along with constraints
        # that describe when each option is possible
        options = drop_skipped([
            # base case
            0 if i == 0 and j == 0 else Skip,
            # align last char of p1 with an inserted gap, so i is decremented but not j
            ed(i-1, j) + 1 if i > 0 else Skip,
            # align last char of p2 with an inserted gap, so j is decremented but not i
            ed(i, j-1) + 1 if j > 0 else Skip,
            # replace last char of p1 with last char of p2
            ed(i-1, j-1) + 1 if j > 0 and i > 0 and s1[i-1] != s2[j-1] else Skip,
            # align last char of p1 with matching last char of p2
            ed(i-1, j-1) if j > 0 and i > 0 and s1[i-1] == s2[j-1] else Skip
        ])
        return min(options)
    return ed(len(s1), len(s2))

# length of longest increasing sub sequence
def LIS(A):

    # make a list of lists
    L = list()
    for i in range(0, len(A)):
        L.append(list())

    # the first increasing subsequence is the first element in A
    L[0].append(A[0])

    for i in range(1, len(A)):
        for j in range(0, i):
            # a new larger increasing subsequence found
            if (A[j] < A[i]) and (len(L[i]) < len(L[j])):
                'throw the previous list'
                L[i] = []
                'add all elements of L[j] to L[i]'
                L[i].extend(L[j])
        L[i].append(A[i])
    return L[-1]


''' The function to find shortest paths from given vertex. 
    It uses recursive topologicalSortUtil() to get topological 
    sorting of given graph.'''
def path(graph, s, V, pathType): 

    # Mark all the vertices as not visited 
    visited = [False]*V 
    stack =[]
    if(pathType == "long"):
        for s in graph:
            val = graph[s][s]
            graph[s][s] = val * -1
    # A recursive function used by shortestPath and longestPath
    @lru_cache(maxsize=None)
    def topologicalSortUtil(v,visited,stack): 

        # Mark the current node as visited. 
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex 
        if v in graph.keys(): 
            for node, weight in graph[v]: 
                if visited[node] == False: 
                    topologicalSortUtil(node,visited,stack) 

        # Push current vertex to stack which stores topological sort 
        stack.append(v)

    # Call the recursive helper function to store Topological 
    # Sort starting from source vertice 
    for i in range(V): 
        if visited[i] == False: 
            topologicalSortUtil(s,visited,stack) 

    # Initialize distances to all vertices as infinite and 
    # distance to source as 0 
    dist = [float("Inf")] * (V) 
    dist[s] = 0

    # Process vertices in topological order 
    while stack: 

        # Get the next vertex from topological order 
        i = stack.pop() 

        # Update distances of all adjacent vertices 
        for node,weight in graph[i]: 
            if dist[node] > dist[i] + weight: 
                dist[node] = dist[i] + weight 

    totalDistance = 0
    # Print the calculated shortest distances 
    for i in range(V):
        if dist[i] != float("Inf"):
            if totalDistance < dist[i]:
                totalDistance = dist[i]
        # print ("%d" %dist[i]) if dist[i] != float("Inf") else  "Inf" , 
    return totalDistance

def TotalPaths(s, d, V, graph): 

    # Mark all the vertices as not visited 
    visited =[False]*(V)
    path = []
    total = 0

    def Paths(u, d, visited): 
    
        # Mark the current node as visited and store in path 
        visited[u]= True
        path.append(u) 

        # If current vertex is same as destination, then print 
        # current path[] 
        if u == d: 
            total = total + 1
            #print (path)
        else: 
            # If current vertex is not destination 
            #Recur for all the vertices adjacent to this vertex 
            for i in graph[u]: 
                if visited[i]==False: 
                    Paths(i, d, visited) 
                        
        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False
    Paths(s,d,visited)
    return total

# loot item for knapsack
Item = namedtuple('Item', ['weight', 'value'])

def test_knapval_rep():
    loot = [
        Item(6, 30),
        Item(3, 14),
        Item(4, 16),
        Item(2, 9),
    ]
    assert knapval_rep(10, loot) == 48

def test_knapval_norep():
    loot = [
        Item(6, 30),
        Item(3, 14),
        Item(4, 16),
        Item(2, 9),
    ]
    assert knapval_norep(10, loot) == 46

def test_edit_distance():
    assert edit_distance("exponential", "polynomial") == 6

def test_LIS():
    A = [3, 5, 10, 0, 1, 100, 2, 4, 7]
    assert LIS(A) == [0, 1, 2, 4, 7]

def test_total_path():
    pass

def test_short_path():
    g = defaultdict(list)
    g[0] = [0,1]
    pass

def test_long_path():
    pass