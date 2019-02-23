# def explore(g, v):
#     """
#     g: adjacency matrix for undirected graph
#     v: a node to start exploring from (an index)
#     """
#     previsit(v)
#     visited[v] = True

#     for b in g[v]:
#         if not visited[b]:
#             explore(g, b)
#         # print(g[v])
#         # print(visited[b])
#     postvisit(v)
    
# def dfs(g):
#     """
#     DepthFirstSearch
#     """
#     # globals()['visited'] = {}

#     visited = [False] * len(g)
#     # print (visited)
#     for v in range(len(g)):
#         if not visited[v]:
#             explore(g, v)