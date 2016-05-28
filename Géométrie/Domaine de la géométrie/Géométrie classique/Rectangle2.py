# -*- coding: utf-8 -*-

import os


class Rectangle2():
    """
    Holds a parallel-axes rectangle by storing lower left point, height and width
    """

    def __init__(self, point, height, width):
        assert isinstance(point, Point)
        assert isinstance(height, (int, float))
        assert isinstance(width, (int, float))
        assert height > 0
        assert width > 0
        self.point = point
        self.height = float(height)
        self.width = float(width)

    def __repr__(self):
        representation = "Rectangle with lower left {0} and upper right {1}"
        return representation.format(self.point, Point(self.point.x + self.width, self.point.y + self.height))

    def dimensions(self):
        return self.height, self.width

    def area(self):
        area = self.height * self.width
        return area

    def transpose(self):
        self.point = Point(self.point.x - self.height,
                           self.point.y - self.width)
        self.height, self.width = self.width, self.height

rec = Rectangle2(Point(), 1, 2)
print(rec)
print("Area:", rec.area())
print("Dimensions:", rec.dimensions())
rec.transpose()
print("Transposed:", rec)

os.system("pause")
