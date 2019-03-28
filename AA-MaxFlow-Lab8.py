from pulp import LpProblem, LpMinimize, LpMaximize, LpVariable
from collections import defaultdict

def vars(s, low=None, high=None):
    """example creates three variables bounded from 0 to 10:
    a, b, c = vars('a,b,c', 0, 10)
    """
    return tuple(LpVariable(v.strip(), low, high) for v in s.split(','))


def lp(mode, objective, constraints):
    """see lp1 below for an example"""
    if mode.lower() == 'max':
        mode = LpMaximize
    elif mode.lower() == 'min':
        mode = LpMinimize
    prob = LpProblem("", mode)
    prob += objective
    for c in constraints:
        prob += c
    prob.solve()
    return prob, prob.objective.value(), dict((v.name, v.value()) for v in prob.variables())


def lp1():
    x_1, x_2 = vars('x_1, x_2')
    return lp('max', x_1 + 6*x_2, [
            x_1 >= 0,
            x_2 >= 0,
            x_1 <= 200,
            x_2 <= 300,
            x_1 + x_2 <= 400])
def lp2():
    x_1, x_2, x_3 = vars('x_1, x_2, x_3', low = 0)
    return lp('max', x_1 + 6*x_2 + 13*x_3, [
            x_1 <= 200,
            x_2 <= 300,
            x_1 + x_2 + x_3 <= 400,
            x_2+3*x_3 <= 600])
def lp3():
    x1, x2, x3, x4, x5, x6 = vars('x1, x2, x3, x4, x5, x6', low = 0)
    return lp('max', 3*x1 + 3*x2 + 2*x3 + 2*x4 + 4*x5 + 4*x6, [
            x1 + x2 + x3 + x4 <= 10,
            x1 + x2 + x5 + x6 <= 12,
            x3 + x4 + x5 + x6 <= 8,
            x1 + x4 + x6 <= 6,
            x2 + x3 + x6 <= 13,
            x2 + x4 + x5 <= 11,
            x1 + x2 >= 2,
            x3 + x4 >= 2,
            x5 + x6 >= 2,])
def lp4():
    x, y = vars('x, y', low = 0)
    return lp('max', x + y, [
            2*x + y <= 3,
            x + 3*y <= 5])

def invertGraph(graph):
    tempGraph = defaultdict(list)
    for value in graph:
        for adjacent in graph[value]:
            tempGraph[adjacent].append(value)
    return tempGraph

def sumEdges(g):
    tempGraph = []
    for i in g:
        for v in range(len(g[i])):
            constraint = constraint + g[i][v][1]
            #print(g[i][v][1])
        tempGraph += constraint
        #print("Constraint: " + str(constraint))
        constraint = 0
        #print("\n")

def InflowOutflow():

    x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = vars('x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10', low = 0)
    return lp('max', x0 + x1 + x2, [
        x0 <= 3,
        x1 <= 3,
        x2 <= 4,
        x3 <= 10,
        x4 <= 2,
        x5 <= 1,
        x6 <= 1,
        x7 <= 5,
        x8 <= 2,
        x9 <= 1,
        x10 <= 5,

        # Sum in to a
        x0 + x3 <= x4,

        # Sum in to b
        x1 <= x3 + x5,

        # Sum in to c
        x2 + x6 <= x7,

        # Sum in to node d
        x4 + x5 <= x6 + x8 + x9,

        # Sum in to e
        x7 + x9 <= x10
    ])

def MaxFlow(graph, start, target):
    """ 
        Takes in graph, start and target nodes.
        Returns 
            1. Dictionary from edges to flow along that edge
            2. A number holding the total flow possible from start to target

    """
    pass

def main():
    g = defaultdict(list)
    g['a'].extend([['d', 2]])
    g['b'].extend([['a', 10], ['d', 1]])
    g['c'].extend([['e', 5]])
    g['d'].extend([['t', 2], ['e', 1], ['c', 1]])
    g['e'].extend([['t', 5]])
    g['s'].extend([['a', 3], ['b', 3], ['c', 4]])

    """
    constraint = 0
    for i in g:
        for v in range(len(g[i])):
            constraint = constraint + 1
            #print(g[i][v][1])        
    print("Constraint: " + str(constraint)) 
    """
    
    #print(lp1())
    #print(lp2())
    #print(lp3())
    print(InflowOutflow())

if __name__ == "__main__":
    main()