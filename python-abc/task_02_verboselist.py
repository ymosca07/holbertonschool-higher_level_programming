#!/usr/bin/env python3
"""Ceci est une description"""


class VerboseList(list):
    """Ceci est une description"""

    def append(self, item):
        """Ceci est une description"""
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, item):
        """Ceci est une description"""
        print(f"Extended the list with [{len(item)}] items.")
        super().extend(item)

    def remove(self, item):
        """Ceci est une description"""
        if item not in self:
            raise ValueError("Can't find this value in this instance")
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, item=-1):
        """Ceci est une description"""
        if self[item] is None:
            raise IndexError("Index does not exist")
        print(f"Popped [{self[item]}] from the list.")
        retour = super().pop(item)
        return retour
