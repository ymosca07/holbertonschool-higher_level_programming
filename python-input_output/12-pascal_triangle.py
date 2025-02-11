#!/usr/bin/python3
"""Ceci est une description"""


def pascal_triangle(n):
    """Ceci est une description"""
    if n <= 0:
        return []

    """Première ligne commence à 1"""
    triangle = [[1]]

    for i in range(1, n):
        """Recupère la ligne précédente"""
        prev_row = triangle[-1]
        """1 a chaque extremité + calcul données prev_row"""
        new_row = [1] + [prev_row[j] + prev_row[j + 1]
                         for j in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle
