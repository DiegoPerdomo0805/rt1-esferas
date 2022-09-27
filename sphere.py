from lib import sum, sub, mul, dot, cross, length, norm

class Sphere(object):
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color


    def ray_intersect(self, o, d):
        L = sub(self.center, o)
        #print(L)
        #print(o)
        #print(d)
        tca = dot(L, d)
        #print(tca)
        l = length(L)
        d_square = l**2 - tca**2
        r_square = self.radius**2
        #print(d_square)
        #print(r_square)
        #print('----------------------------------------------------------------------------')
        if d_square > r_square:
            #print("d_square > r_square")
            return False
        thc = (self.radius**2 - d_square)**0.5
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return False
        return True
    
    


