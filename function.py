from utils import *

class Fx(object):
    """Object representation for a function"""
    def __init__(self, f):
        super(Fx, self).__init__()
        self.f = f

    # return the value at the arguments
    def val(self, *args):
        return self.f(*args)


if __name__ == '__main__':
    f = Fx(lambda x = 0, y = 0: x*x + y)
    print f.val(3, 8)