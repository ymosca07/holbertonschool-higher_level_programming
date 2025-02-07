#!/usr/bin/env python3
"""Ceci est une description"""


class Fish:
    """Ceci est une description"""
    def swim(self):
        print("The fish is swimming")
    def habitat(self):
        print("The fish lives in water")

class Bird:
    """Ceci est une description"""
    def fly(self):
        print("The bird is flying")
    def habitat(self):
        print("The bird lives in the sky")
    
class FlyingFish(Fish, Bird):
    """Ceci est une description"""
    def fly(self):
        print("The flying fish is soaring!")
    def swim(self):
        print("The flying fish is swimming!")
    def habitat(self):
        print("The flying fish lives both in water and the sky!")
