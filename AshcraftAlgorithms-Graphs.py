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

class Graph:
    def __init__(self, al):
        self.graph = al
        self.preClock = 0
        self.postClock = 0
        self.tracker = defaultdict(list)

    def previsit(self, v):
        print("previsit visiting: %s" %v)
        
    def postvisit(self, v):
        print("done visiting: %s" % v)

    def invert(self):
        tempGraph = defaultdict(list)
        for value in self.graph:
            for adjacent in self.graph[value]:
                tempGraph[adjacent].append(value)
        return tempGraph

    def DFSUtil(self,v,visited, graph):
        visited[v]= True
        print (v)
        for i in graph[v]: 
            self.preClock += 1
            if visited[i] == False: 
                self.DFSUtil(i, visited, graph)
            self.postClock += 1
        self.tracker[v].append(self.preClock)
        self.tracker[v].append(self.postClock)

    # Pass in what node you want to start on defaults to 0
    def DFS(self, v = 0):   
        visited = [False]*(len(self.graph)) 
        self.DFSUtil(v,visited, self.graph)
        return self.tracker

    # Pass in what node you want to start on defaults to 0
    def reverseDFS(self, v = 0):   
        visited = [False]*(len(self.graph)) 
        self.DFSUtil(v,visited, self.invert())
        return self.tracker

def test_adj_inverse():
    g = defaultdict(list)
    g[0].extend([1,2])
    g[1].extend([2])
    g[2].extend([0])
    g2 = defaultdict(list)
    g2[0].extend([2])
    g2[1].extend([0])
    g2[2].extend([0,1])
    adj = Graph(g)
    tempGraph = adj.invert()
    assert tempGraph == g2

def test_depth_first_search():
    g = defaultdict(list)
    g[0].extend([1,2])
    g[1].extend([2])
    g[2].extend([0])
    graph = Graph(g)

    # Index is node
    # The first in the list is previsit
    # The next in the list is postvisit
    explored = defaultdict(list)
    explored[0].extend([4,4])
    explored[1].extend([4,2])
    explored[2].extend([4,3])
    assert graph.reverseDFS() == explored

if __name__ == "__main__":
    g = defaultdict(list)
    g[0].extend([1,2])
    g[1].extend([2])
    g[2].extend([0])
    tempGraph = Graph(g)
    print(tempGraph.invert())
    value = tempGraph.DFS()
    print(value)