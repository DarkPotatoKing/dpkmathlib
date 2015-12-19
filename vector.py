from utils import *

class Vector(object):
    """Vector object representation"""
    def __init__(self, *args):
        super(Vector, self).__init__()
        args = [float(i) for i in args]
        self.args = args

    # return a string representation in vector notation
    def __repr__(self):
        return '<' + ', '.join([str(i) for i in self.args]) + '>'

    # return the magnitude of the vector
    def magnitude(self):
        return math.sqrt(sum([i*i for i in self.args]))

    # return a normalized version of the vector
    def normalize(self):
        m = self.magnitude()
        return Vector(*[i/m for i in self.args])

    # return a deep copy of the vector
    def copy(self):
        return copy.deepcopy(self)

    # return the dot product with another vector
    def dot(self, other):
        a = self.copy()
        b = other.copy()
        Vector.equalize_dimensions(a, b)
        return sum([a[i] * b[i] for i in xrange(len(a))])

    # return a unit vector with an angle theta
    @classmethod
    def unit(cls, theta):
        return Vector(sin(theta), cos(theta))

    # convert 2 vectors into vectors of the same dimension
    # (return nothing)
    @classmethod
    def equalize_dimensions(cls, a, b):
        dimension = max([len(a), len(b)])
        a.args = a.args + [0] * (dimension - len(a))
        b.args = b.args + [0] * (dimension - len(b))

    # set the value of a dimension vector
    def __setitem__(self, index, value):
        self.args[index] = value

    # get the value of a dimension vector
    def __getitem__(self, index):
        return self.args[index]

    # return the number of dimensions of the vector
    def __len__(self):
        return len(self.args)

    # return the result of vector addition
    def __add__(self, other):
        a = self.copy()
        b = other.copy()
        Vector.equalize_dimensions(a, b)
        return Vector(*[a[i] + b[i] for i in xrange(len(a))])

    # return the result of vector subtraction
    def __sub__(self, other):
        return self + other * -1

    # return a vector scaled by the multiplier
    def __mul__(self, multiplier):
        return Vector(*[i * multiplier for i in self.args])

    # return a vector scaled by the divisor
    def __truediv__(self, divisor):
        return Vector(*[i / divisor for i in self.args])


if __name__ == '__main__':
    a = Vector(1,2,3)
    b = Vector(4,5)
    print a.dot(b)
    print b.dot(a)