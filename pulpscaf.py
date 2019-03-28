from pulp import LpProblem, LpMinimize, LpMaximize, LpVariable


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

def InflowOutflow(graph):
    x1, x2, x3, x4, x5, x6 = vars('x1, x2, x3, x4, x5, x6', low = 0)
    pass


def main():
    
    #print(lp1())
    #print(lp2())
    #print(lp3())
    print(lp4())

if __name__ == "__main__":
    main()