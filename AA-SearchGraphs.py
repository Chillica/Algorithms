# -*- coding: utf-8 -*-
"""
Jacob Ashcraft
Graphs - Using Priority Queue for DFS, BFS, Dykstra's, A* (Star Search)
Advanced Algorithms
Professor Teichert

"""

from boltons.queueutils import PriorityQueue
from collections import defaultdict


class Graph:
    def __init__(self, adjList, nodes = 0):
        self.graph = adjList
        self.nodes = nodes
        self.s = 0
        self.t = 0

    def setSearch(self, s = 0, t = 0):
        """
            Takes in s (start) and t (end) nodes.
            Validates that start and end are within the number of nodes of the graph.
        """
        if s < self.nodes and s > 0:
            self.s = s
        if t < self.nodes and t > 0:
            self.t = t

    def path(self, destNode, parents):
        print("Start: "+ str(self.s) +". Destination: " + str(destNode) + ". Visited: " + str(parents))

    def heuristic(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def cost(self, cur, next):
        return 0

    def dijsktra(self):
        """
            dijsktra's search starts with node s, and ends with node t.
        """
        clock = 0
        #cost = {}
        visited = {}
        q = PriorityQueue()
        q.add(self.s, priority = 0)

        while q is not None:
            p = q.pop()
            if p == self.t:
                return self.path(p, visited)
            for b in self.graph[p]:
                visited[b] = p
                q.add(b, priority = clock - 1)
                clock += 1
        return self.path(-1, 0)

    def dfs(self):
        """
            dfs (depth first search) starts with node s, and ends with node t.
        """
        visited = set()
        q = PriorityQueue()
        q.add(self.s, priority = 0)

        while q:
            current = q.pop()
            if current not in visited:
                visited.add(current)
                if current == self.t:
                    return self.path(current, visited)
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        q.add(neighbor)
        return self.path(-1, 0)

    def bfs(self):
        """
            bfs (breadth first search) starts with node s, and ends with node t.
        """
        visited = set()
        q = PriorityQueue()
        q.add(self.s, priority = 0)
        clock = 0

        while q:
            current = q.pop()
            if current not in visited:
                visited.add(current)
                if current == self.t:
                    return self.path(current, visited)
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        q.add(neighbor, priority = clock - 1)
                        clock += 1
        return self.path(-1, 0)

    def ss(self):
        """
            SS (Star Search) starts with node s, and ends with node t.
        """
        q = PriorityQueue()
        q.add(self.s, 0)
        came_from = {}
        cost_so_far = {}
        came_from[self.s] = None
        cost_so_far[self.s] = 0
        
        while q:
            current = q.pop()
            if current == self.t:
                return self.path(came_from, cost_so_far)
            for next in self.graph[current]:
                new_cost = cost_so_far[current] + self.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(self.t, next)
                    q.add(next, priority)
                    came_from[next] = current
        return self.path(-1, 0)

    def DFS(self):
        pass

    def BFS(self):
        pass

    def Dykstra(self):
        pass

    def StarSearch(self):
        pass


if __name__ == "__main__":
    adjList = defaultdict(list)
    adjList[0] = [1,2]
    adjList[1] = [0,2]
    adjList[2] = [1]
    graph = Graph(adjList,3)
    graph.setSearch(2,1)
    graph.dijsktra()
    graph.dfs()
    graph.bfs()
    
    adjList2 = defaultdict(list)
    adjList2[0] = [1]
    adjList2[1] = [0, 2, 3]
    adjList2[2] = [0]
    adjList2[3] = [4, 0]
    adjList2[4] = [2]

    graph = Graph(adjList2, 5)
    graph.setSearch(4,3)
    graph.bfs()
    graph.dfs()
    graph.bfs()

    edges = {
        0: [1],
        1: [0, 2, 3],
        2: [0],
        3: [4, 0],
        4: [2]
    }
    graph = Graph(edges, 5)
    graph.ss()