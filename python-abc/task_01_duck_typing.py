#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius
    
    def area(self):
        return math.pi * (self.__radius * self.__radius)

    def perimeter(self):
        return 2 * math.pi * self.__radius

class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width
    
    def perimeter(self):
        return (2 * self.__height) + (2 * self.__width)
    
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
