# bicikli-kölcsönző rendszer

class Bicikli:
    def __init__(self, tipus, ar, allapot):
        self.tipus = tipus
        self.ar = ar
        self.allapot = allapot


class Kolcsonzo:
    pass


class Kolcsonzes:
    pass

hegyi = Bicikli("hegyi kerékpár", 1500, "normál")
orszaguti = Bicikli("orszaguti kerékpár", 1800, "normál")
gyermek = Bicikli("gyermek kerékpár", 1000, "normál")