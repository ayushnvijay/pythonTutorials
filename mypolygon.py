from swampy.TurtleWorld import *
import math

"""Doc String"""
world = TurtleWorld()
bob = Turtle()
print bob

def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        lt(t,360/n)
polygon(bob, 80, 5)

def circle(turtle, radius):
    circumference = math.pi*2*radius
    n = 50
    length = circumference/n
    polygon(turtle,length,n)
circle(bob, 100)
print "drawing polygon"
