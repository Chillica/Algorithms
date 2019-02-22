# Jed Black
# February 15, 2019
# This file contains a lab about strongly connected components of a graph.
# There are many problems with graphs, in this lab we aim to solve the porblem
# our solution will work on either directed or undirected graphs

# Disclaimer: some of this lab doesn't work, 
# but I put lots of hours into trying!!!
 
#Using the DefaultDict
from collections import defaultdict

#################################################################################################
# Search the Node made for DFS
#################################################################################################
class Search:
    def __init__(self,value):
        self.value = value
        self.before = None
        self.after = None

#################################################################################################
# Take an adjacency list representation of a graph returns reversed
#################################################################################################
def reverseAdjacentList(adjacencyList):
    reversedList = defaultdict(list)
    for nodeOne, values in adjacencyList.items():
        for value in values:
            reversedList[value].append(nodeOne)
    return reversedList

#################################################################################################
# Depth First Search -- This doesn't work! --
#################################################################################################  
def dFS(adjacencyList, node, clockNumber = 0):
    visited = [False]*len(adjacencyList)
    visited[node] = True
    SearchList = list()
    nodeValues = Search(node)
    nodeValues.before = clockNumber
    clockNumber +=1

    for v in adjacencyList[node]:
        if visited[v] == False:
            dFS(adjacencyList, v, clockNumber)
    nodeValues.after = clockNumber
    clockNumber+=1
    SearchList.append(nodeValues)

    return SearchList

#################################################################################################
# Testing reversed graph function
#################################################################################################
def test_reverse_directedGraph():
    adjacentList = [(1,2),(2,3),(4,5),(5,6),(6,4),(4,1)]
    originalGraph = defaultdict(list)
    for nodeOne, nodeTwo in adjacentList:
        originalGraph[nodeOne].append(nodeTwo)

    reversedList = [(1,4),(2,1),(3,2),(4,6),(5,4),(6,5)]
    reversedGraph = defaultdict(list)

    for nodeOne, nodeTwo in reversedList:
        reversedGraph[nodeOne].append(nodeTwo)

    assert reverseAdjacentList(originalGraph) == reversedGraph

#################################################################################################
# Testing the Reverse graph and the Adjacent List
#################################################################################################
def test_reverse_undirectedGraph():
    adjacentList = [(0,1),(0,4),(1,0),(1,4),(1,2),(1,3),(2,1),(2,3),(3,1),(3,4),(3,2),(4,3),(4,0),(4,1)]
    originalGraph = defaultdict(list)
    
    for nodeOne, nodeTwo in adjacentList:
        originalGraph[nodeOne].append(nodeTwo)
    assert sorted(reverseAdjacentList(originalGraph)) == sorted(originalGraph)

#################################################################################################
#Testing the depth-first search
#################################################################################################
if __name__ == "__main__":
    adjacentList = [(1,2),(2,3),(4,5),(5,6),(6,4),(4,1)]
    originalGraph = defaultdict(list)
    for nodeOne, nodeTwo in adjacentList:
        originalGraph[nodeOne].append(nodeTwo)
    
    print("The Original graph: ")
    print(originalGraph.items())

    reversedGraph = reverseAdjacentList(originalGraph)
    print("The Reversed graph: ")
    print(reversedGraph.items())
    
    dfsResults = dFS(originalGraph, next(iter(originalGraph)))
    print(dfsResults[0].after)
    print(dfsResults[2].after)