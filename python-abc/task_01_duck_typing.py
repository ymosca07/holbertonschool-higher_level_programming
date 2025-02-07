#!/usr/bin/python3
"""Ceci est une description"""
from abc import ABC, abstractmethod
import math
"""Ceci est une description"""


class Shape(ABC):
    """Ceci est une description"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Ceci est une description"""
    def __init__(self, radius=0):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        self.radius = abs(radius)

    def area(self):
        return (math.pi * (self.radius**2))

    def perimeter(self):
        return (2 * math.pi * self.radius)


class Rectangle(Shape):
    """Ceci est une description"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return ((2 * self.width) + (2 * self.height))


def shape_info(forme):
    if hasattr(forme, 'area') and hasattr(forme, 'perimeter'):
        area = forme.area()
        perimeter = forme.perimeter()
        print("Area: {}".format(area))
        print("Perimeter: {}".format(perimeter))
    else:
        raise AttributeError("No such attribute")
