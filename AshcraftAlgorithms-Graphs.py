# -*- coding: utf-8 -*-
"""
Jacob Ashcraft
Graphs - Strongly Connected Components
Advanced Algorithms
Professor Teichert

"""
from collections import defaultdict
# Hold a map from vertex (int)
# to boolean indicating if we have visited
# that node
visited = {}
clock = 0

def previsit(v):
    print("previsit visiting: %s" %v)
def postvisit(v):
    print("done visiting: %s" % v)

def explore(g, v):
    """
    g: adjacency matrix for undirected graph
    v: a node to start exploring from (an index)
    """
    #previsit(v)
    visited[v] = True
    previsit(v)
    print(g)
    print(v)
    print (visited)
    """ for b in g[v]:
        if not visited[b]:
            explore(g, b) """
    postvisit(v)
    
def dfs(g):
    """
    DepthFirstSearch
    """
    globals()['visited'] = {}

    visited = [False] * len(g)
    print (visited)
    for v in range(len(g)):
        if not visited[v]:
            explore(g, v)

if __name__ == "__main__":
    g = defaultdict(list)
    g[0].extend([1,2])
    g[1].extend([0,3,4])
    g[2].extend([0,3])
    g[3].extend([1,2,4])
    g[4].extend([1,3])
    dfs(g)