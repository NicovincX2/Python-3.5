# -*- coding: utf-8 -*-

import os

class Rectangle1():
    """
    Holds a parallel-axes rectangle by storing two points
    lower left vertex - llv
    upper right vertex - urv
    """
    def __init__(self, lower_left_vertex, upper_right_vertex):
        assert isinstance(lower_left_vertex, Point)
        assert isinstance(upper_right_vertex, Point)
        assert lower_left_vertex < upper_right_vertex 
        self.llv = lower_left_vertex
        self.urv = upper_right_vertex
        
    def __repr__(self):
        representation = "Rectangle with lower left {0} and upper right {1}"
        return representation.format(self.llv, self.urv)

    def dimensions(self):
        height = self.urv.y - self.llv.y
        width = self.urv.x - self.llv.x
        return height, width
    
    def area(self):
        height, width = self.dimensions()
        area = height * width
        return area
    
    def transpose(self):
        """
        Reflection with regard to the line passing through lower left vertex with angle 315 (-45) degrees
        """
        height, width = self.dimensions()
        self.urv = self.llv
        self.llv = Point(self.urv.x - height, self.urv.y - width)

rec = Rectangle1(Point(), Point(2,1))
print(rec)
print("Area:", rec.area())
print("Dimensions:", rec.dimensions())
rec.transpose()
print("Transposed:", rec)

os.system("pause")