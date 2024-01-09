from abc import ABC, abstractmethod
from datetime import datetime


class Bicikli:
    def __init__(self, tipus, ar, allapot):
        self.tipus = tipus
        self.ar = ar
        self.allapot = allapot

    @abstractmethod
    def arkalkulacio(self):
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
    def __init__(self, bicikli, datum):
        self.bicikli = bicikli
        self.datum = datum

    def ar(self):
        return self.bicikli.arkalkulacio()

    def lemondas(self):
        self.bicikli.allapot = "Elérhető"

    def __str__(self):
        return f"{self.bicikli.tipus} - {self.datum.strftime('%Y-%m-%d')} - {self.ar()} Ft"


class Kolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.kerekparok = []
        self.esemenyek = []

    def __add__(self, other):
        if isinstance(other, Bicikli):
            self.kerekparok.append(other)
        else:
            print("Ez nem Kerékpár")

    def keres(self, tipus):
        for bicikli in self.kerekparok:
            if bicikli.tipus == tipus and bicikli.allapot == "Elérhető":
                return bicikli
        return None

# ESEMÉNY metódusok

    # Biciklik kölcsönzésének lehetősége egy adott napra, a kölcsönzés árának kiszámításával. (15 pont)
    def kolcsonzes(self, bicikli, datum):
        if bicikli.allapot == "Elérhető" and datum >= datetime.now():
            bicikli.allapot = "Nem elréhető"
            kolcsonzes = Kolcsonzes(bicikli, datum)
            self.esemenyek.append(kolcsonzes)
            return f"{bicikli.tipus} kölcsönzése megtörtént. Fizetendő: {kolcsonzes.ar()} Ft."
        else:
            return "Hibás dátum, vagy nem eléhető."

    # Kölcsönzések lemondásának lehetősége. (5 pont)
    def lemondas(self, kolcsonzes):
        if kolcsonzes in self.esemenyek and kolcsonzes.datum >= datetime.now():
            kolcsonzes.lemondas()
            self.esemenyek.remove(kolcsonzes)
            return f"{kolcsonzes.bicikli.tipus} lemondva."
        else:
            return "Nincs ilyen esemény."

    # Kölcsönzések listázásának lehetősége. (5 pont)
    def listazas(self):
        if self.esemenyek:
            for kolcsonzes in self.esemenyek:
                print(kolcsonzes)
        else:
            print("Hiba.")


# Készíts egy egyszerű felhasználói interfészt (20 pont)

def interfesz():
    pass