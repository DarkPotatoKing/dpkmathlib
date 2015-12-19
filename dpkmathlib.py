from function import *
from vector import *

if __name__ == '__main__':
    f = Fx(lambda r, o: e**-r * sin(o))
    print f.du(Vector(3,-2), 0, pi/3)
    print 3/sqrt(13)*-sqrt(3)/2-2/sqrt(13)*1/2