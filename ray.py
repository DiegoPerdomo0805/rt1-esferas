from lib import *
import random
from sphere import Sphere
from math import *

class RayTracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear_color = color(0, 0, 0)
        self.current_color = color(255,255, 255)
        self.background_color = color(0, 0, 0)
        self.dense = 1
        self.scene = []
        self.clear()

    def clear(self):
        self.framebuffer = [
            [self.clear_color for x in range(self.width)] 
            for y in range(self.height)
            ]

    def point(self, x, y, c = None):
        if y > 0 and y < self.height and x > 0 and x < self.width:
            if c is None:
                c = self.current_color
            self.framebuffer[y][x] = c
    
    def write(self, filename):
        writebmp(filename, self.width, self.height, self.framebuffer)

    def color(self, r, g, b):
        self.current_color = color(r, g, b)    

    def cast_ray(self, origin, direction):
        for s in self.scene:
            i = s.ray_intersect(origin, direction)
            if i:
                return s.color
        return self.background_color


    def render(self):
        fov = int(pi / 2)
        aspect_ratio = self.width / self.height
        #angle = tan(fov / 2)
        angle = tan(fov / 2)

        #cara
        self.scene.append(Sphere(V3(0.5,-3.375,-14), 0.15, color(0 , 0, 0)))
        self.scene.append(Sphere(V3(-0.5,-3.375,-14), 0.15, color(0 , 0, 0)))
        self.scene.append(Sphere(V3(0,-3,-14), 0.15, color(252,76,2)))

        

        #botones
        self.scene.append(Sphere(V3(0,-0.5,-14), 0.375, color(157,34,53)))
        self.scene.append(Sphere(V3(0,0.5,-14), 0.375, color(157,34,53)))
        self.scene.append(Sphere(V3(0,1.5,-14), 0.375, color(157,34,53)))

        #Bolas de nieve
        self.scene.append(Sphere(V3(0,4,-14), 3, color(255,255,255)))
        self.scene.append(Sphere(V3(0,-0.125,-14), 2, color(255,255,255)))
        self.scene.append(Sphere(V3(0,-3,-14), 1, color(255,255,255)))        


        for y in range(self.height):
            for x in range(self.width):
                rand = random.uniform(0, 1)
                if rand < self.dense:
                    i = ((2 * (x + 0.5) / self.width) - 1) * angle * aspect_ratio
                    j = (1 - 2 * (y + 0.5) / self.height) * angle 
                    
                    direction = V3(i, j, -1).norm()
                    origin = V3(0, 0, 0)
                    
                    c = self.cast_ray(origin, direction)
                    #c = color(255,0,0)
                    self.point(x, y, c)
                
        self.write('ray.bmp')
    
    
    
    #def raytrace(self, x, y):
    #    return (0, 0, 0)

#r = RayTracer(500, 500)
#r.point(10, 10)
#r.dense = 0.1
#r.render()
#