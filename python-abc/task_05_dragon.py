#!/usr/bin/python3
"""Ceci est une description"""


class SwimMixin:
    """Ceci est une description"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Ceci est une description"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Ceci est une description"""
    def roar(self):
        print("The dragon roars!")