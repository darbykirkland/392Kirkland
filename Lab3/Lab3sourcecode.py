# Lab3 Darby Kirkland

# Read data in from the provided text file (20 pt)
# Create a class for each shape found in the text files (20 pt)
# For each line, create a new obect determined by the shape (e.g., Triangle, 8, 1 base and height) (30pt)
# Iterate through your list and print out the area for each shape (30pt)
 
#import library for pi
import math

#create and define classes
class shape:
    def __init__init(self):
        pass
    def getArea(self):
        pass

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def getArea(self):
        return self.length * self.width
        
class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def getArea(self):
        return (self.base * self.height)/2
        
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return (self.radius * self.radius * math.pi)


# open the text file containing the shapes
file = open(r'C:\Users\spygo\Desktop\Repos\GEOG392\Lab3\shapes.txt')
lines = file.readlines()
file.close()

# for each line, print area
for line in lines:
    components = line.split(",")

    if components[0] == "Rectangle":
        r = rectangle(float(components[1]),float(components[2]))
        print(r.getArea())
    elif components[0] == "Triangle":
        t= triangle(float(components[1]),float(components[2]))
        print(t.getArea())
    else:
        c = circle(float(components[1]))
        print(c.getArea())