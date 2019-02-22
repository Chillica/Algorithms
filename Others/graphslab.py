from collections import defaultdict

class SearchNode:
    index = 0
    preClock = 0
    postClock = 0

def reverse_graph(adj_list):
    for i in range(0, len(adj_list)):
        adj_list[i] = (adj_list[i][1], adj_list[i][0])

def depth_first_search(adj_list, next, visited, reverse_graph, search_node):
    globals()['visited'] = {}

    visited = [False] * len(adj_list)

    search_node = defaultdict(list)
    reverse_graph = defaultdict(list)

    for next in range(len(adj_list)):
        if not visited[next]:
            reverse_graph, search_node = depth_first_search(adj_list, next, visited, reverse_graph, search_node)
    return reverse_graph, search_node

def test_reverse_list():
    adj_list = defaultdict(list)
    adj_list[0] = (0, 1)
    print(reverse_graph(adj_list))

def test_dfs():
    adj_list = defaultdict(list)
    adj_list[0] = (0, 1)
    list(depth_first_search(adj_list, adj_list.next, None, reverse_graph(adj_list), search_node))

test_reverse_list()
test_dfs()