class Polynomial:
    def __init__(self, cs):
        """
        initialize polynomial with coefficients: css
        """
        self.coefficients = cs

    #@staticmethod
    def pad(self, m=0):
        """
        returns a new list with the elements of a padded out to size m with 0
        """
        return list(self.coefficients) + [0] * m

    def __call__(self, x):
        """
        returns p(x)
        """
        return sum(ci*x**i for i, ci in enumerate(self.coefficients))

    def __add__(self, rhs):
        """
        return Polynomial([])
        """
        size = len(self) - len(rhs)
        if size > 0:
            rhs.coefficients = rhs.pad(size)
        elif size < 0:
            self.coefficients = self.pad(abs(size))

        val = []
        i = 0
        for ai, bi in zip(self.coefficients, rhs.coefficients):
            val.insert(i, ai + bi)
            i += 1
        return Polynomial(val)

    def __mul__(self, rhs):
        return Polynomial([])

    def __repr__(self):
        return ' + '.join('%s*x^%s' % (ci, i) for i, ci in enumerate(self.coefficients))

    def __len__(self):
        return len(self.coefficients)

# zip(a, b)
# for ai, bi in zip([4,2,7], [9,3,7,10,100])
#
# enumerate(a)
# max()
# abs()
# sum()

def test_call():
    p = Polynomial([2,3,4])
    val = p(x=2)
    assert val == 2+3*2+4*2**2
    assert val == "2x^0+3x^1+4x^2"

def test_add0():
    p1 = Polynomial([2])
    p2 = Polynomial([3])
    assert (p1+p2).coefficients == [5]

if __name__ == '__main__':
    p1 = Polynomial([1,2,3,4,5])
    p2 = Polynomial([1,2,3,4])
    p3 = Polynomial([1,2])
    print (p1)
    print (p2)
    print (p3)
    p4 = p1 + p2 + p3
    print (p4)