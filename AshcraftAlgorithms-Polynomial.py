class Polynomial:
    def __init__(self, cs):
        """
        initialize polynomial with coefficients: css
        """
        self.coefficients = cs

    def padRight(self, m=0):
        """
        returns a new list with the elements of a padded out to size m with 0
        """
        self.coefficients = list(self.coefficients) + [0] * m

    def padLeft(self, m=0):
        """
        returns a new list with the elements of a padded out to size m with 0
        """
        self.coefficients = ([0] * m) + list(self.coefficients)

    def __call__(self, x):
        """
        returns p(x)
        """
        return sum(ci*(x**i) for i, ci in enumerate(self.coefficients))

    def __add__(self, rhs):
        """
        return Polynomial([])
        """
        size = len(self) - len(rhs)
        if size > 0:
            rhs.padRight(size)
        elif size < 0:
            self.padRight(abs(size))

        val = []
        i = 0
        for ai, bi in zip(self.coefficients, rhs.coefficients):
            val.insert(i, ai + bi)
            i += 1
        return Polynomial(val)

    def __mul__(self, rhs):
        poly = Polynomial([0])
        outerList = []
        innerList = []
        for i, ci in enumerate(self.coefficients):
            for g, cg in enumerate(rhs.coefficients):
                innerList.insert(g, ci * cg)
            tempPoly = Polynomial(innerList)
            tempPoly.padLeft(i)
            outerList.insert(i, tempPoly)
            innerList = []
        
        for i, ci in enumerate(outerList):
            poly += ci

        return poly

    def __repr__(self):
        return ' + '.join('%s*x^%s' % (ci, i) for i, ci in enumerate(self.coefficients))

    def __len__(self):
        return len(self.coefficients)

def test_call():
    p = Polynomial([2,3,4])
    x0 = p(x=0)
    x1 = p(x=1)
    x2 = p(x=2)
    x3 = p(x=-1)
    x4 = p(x=-2)
    assert x0 == 2+0*1+4*0**2 
    assert x1 == 2+3*1+4*1**2
    assert x2 == 2+3*2+4*2**2
    assert x3 == 2+3*(-1)+4*(-1)**2
    assert x4 == 2+3*(-2)+4*(-2)**2

def test_add():
    p1 = Polynomial([2])
    p2 = Polynomial([3])
    p3 = Polynomial([3,3])
    p4 = Polynomial([1,1,1])
    assert (p1+p2).coefficients == [5]
    assert (p2+p3).coefficients == [6,3]
    assert (p3+p4).coefficients == [4,4,1]
    assert (p1+p2+p3+p4).coefficients == [9,4,1]

def test_mul():
    p1 = Polynomial([1,2])
    p2 = Polynomial([1,2,3])
    assert [1,4,4] == (p1 * p1).coefficients
    assert [1,4,7,6] == (p1 * p2).coefficients

def test_all():
    p1 = Polynomial([1,2])
    assert [2,6,4] == (p1 * p1 + p1).coefficients
    assert 12 == (p1 * p1 + p1)(1)

if __name__ == '__main__':
    p1 = Polynomial([1,2,3,4,5])
    p2 = Polynomial([1,2,3])
    p3 = Polynomial([0,2])
    #print (p1)
    #print (p2)
    #print (p3)
    #p4 = p1 + p2 + p3
    #print (p4)
    p5 = p3 * p3 + p3
    p6 = p5(2)
    print (p5)
    print (p6)