from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Bicikli:
    def __init__(self, tipus, ar, allapot):
        self.tipus = tipus
        self.ar = ar
        self.allapot = allapot

    @abstractmethod
    def arkalkulacio (self):
        pass

    def __str__(self):
        return f"{self.tipus}, ára egy napra: {self.ar}"


class Hegyi(Bicikli):
    def arkalkulacio(self):
        return self.ar


class Orszaguti(Bicikli):
    def arkalkulacio(self):
        return self.ar * 1.15


class Gyermek(Bicikli):
    def arkalkulacio(self):
        return self.ar * 0.80


class Kolcsonzes:
    pass


class Kolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.kerekparok = []
        self.esemeny = []

    def __add__(self, other):
        if isinstance(other, Bicikli):
            self.kerekparok.append(other)
        else:
            print("Nem Kerékpár")

    def keres(self, tipus):
        for bicikli in self.kerekparok:
            if bicikli.tipus == tipus and bicikli.allapot == "Elérhető":
                return bicikli
        return None
