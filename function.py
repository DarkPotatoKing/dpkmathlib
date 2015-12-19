from utils import *
from vector import Vector

class Fx(object):
    """Object representation for a function"""
    def __init__(self, f):
        super(Fx, self).__init__()
        self.f = f

    # return the value at the arguments
    def val(self, *args):
        return self.f(*args)

    # return the value of the directional derivative at a point in the direction of u
    def du(self, u, *args):
        u = u.normalize()
        h = 1e-8
        fh_args = [args[i] + h*u[i] for i in xrange(len(args))]
        return (self.val(*fh_args) - self.val(*args)) / h

    # return the value of the partial derivative wrt x at a point
    def dx(self, *args):
        return self.du(Vector(1,0), *args)

    # return the value of the partial derivative wrt y at a point
    def dy(self, *args):
        return self.du(Vector(0,1), *args)


if __name__ == '__main__':
    f = Fx(lambda x = 0, y = 0: x*x + y)
    print f.val(3, 8)