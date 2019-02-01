class Polynomial:
    def __init__(self, cs):
        """
        initialize polynomial with coefficients: css
        """
        self.coefficients = cs

    @staticmethod
    def pad(a, m=0):
        """
        returns a new list with the elements of a padded out to size m with 0
        """
        return list(a) + [0] * (m-len(a))

    def __call__(self, x):
        """
        returns p(x)
        """
        return sum(c*x**i for i, c in enumerate(self.coefficients))

    def __add__(self, rhs):
        """
        return Polynomial([])
        """
        for ai, bi in zip(self.coefficients, rhs):
            print(ai + bi)
        # val = ai + bi
        return Polynomial(val)

    def __mul__(self, rhs):
        return Polynomial([])

# zip(a, b)
# for ai, bi in zip([4,2,7], [9,3,7,10,100])
#
# enumerate(a)
# max()
# abs()
# sum()

def test_call:
    p = Polynomial([2,3,4])
    val = p.__call__
    assert val == "2x^0+3x^1+4x^2"

def test_add0:
    p1 = Polynomial([2])
    p2 = Polynomial([3])
    assert (p1+p2).coefficients == [5]

if __name__ == '__main__'
    p = Polynomial([1,5,6])
    p2 = p + p
    p3 = p * p2
    v = p3(45, 8)