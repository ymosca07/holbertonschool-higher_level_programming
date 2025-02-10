#!/usr/bin/python3
"""Définition de la classe Student"""


class Student:
    """Classe Student avec sérialisation et désérialisation"""
    def __init__(self, first_name, last_name, age):
        """Initialisation des attributs de l'étudiant"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retourne un dictionnaire des attributs de l'instance"""
        if isinstance(attrs, list):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Remplace les attributs de l'instance à partir d'un dictionnaire JSON"""
        for key, value in json.items():
            setattr(self, key, value)
