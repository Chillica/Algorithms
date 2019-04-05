from pulp import LpProblem, LpMinimize, LpMaximize, LpVariable, LpBinary, LpContinuous, LpSolverDefault
from collections import defaultdict
from functools import reduce

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
    #LpSolverDefault.msg = 1
    print(prob.variables)
    prob.solve()
    return prob, prob.objective.value(), dict((v.name, v.value()) for v in prob.variables())

def ilp_sat(expression):
    """ 
        Takes an expression.
        Returns 
            0 or a 1 depending on if there is success or not.

    """
    numVar = []
    variables = []
    variables1 = []
    constraints = []
    andlist = []

    def notMethod(a):
        result = LpVariable("not" + str(len(numVar)), lowBound = 0,  upBound = 1, cat = LpBinary)
        constraints.append(result == 1 - a)

    # def orMethod(a, b):
    #     result = LpVariable("or" + str(len(constraints)), lowBound = 0,  upBound = 1, cat = LpBinary)
    #     constraints.append(result >= a)
    #     constraints.append(result >= b)
    #     constraints.append(result <= a + b)
    #     andlist.append(result)

    # def andMethod(a, b):
    #     result = LpVariable("and" + str(len(numVar)), lowBound = 0, upBound = 1, cat = LpBinary)
    #     constraints.append(result <= a)
    #     constraints.append(result <= b)
    #     constraints.append(result >= a + b - 1)


    # for item in expression:
    #     for v in item.split(','):
    #         if(not(v in numVar)):
    #             numVar.append(v)
    #             temp = LpVariable(v.strip(), 0, 1, cat = LpBinary)
    #             variables.append(temp)
    #             variables1.append(LpVariable(v.strip(), 0, 1, cat = LpBinary))
    #             if v[0] == '-':
    #                 notMethod(temp)
    #         else:
    #             temp = numVar.index(v)
    #             variables.append(variables1[temp])
    #     reduce(orMethod, variables)
    #     variables = []
    # reduce(andMethod, andlist)
    for item in expression:
        for v in item.split(','):
            temp = ''
            if(v[0] == '-'):
                temp = v[1]
            else:
                temp = v
            if not(temp in numVar):
                lpvar = LpVariable(temp.strip(), 0, 1, cat = LpBinary)
                numVar.append(temp)
                notMethod(lpvar)
                constraints.append(lpvar)
    print(numVar)
    print(constraints)
    #print(constraints)
    #print(lp('max', 1, constraints))

def test_ipssat():
    pass

def main():
    ilp_sat(['a,b,c', '-a,b,-c', '-d,-b', '-a,c', '-b,a'])
    #ilp_sat(['a,-b,c', 'b,c,d'])


if __name__ == "__main__":
    main()