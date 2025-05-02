class Ser:
    def __init__(self, nom, edad, masa):
        self.nom = nom
        self.edad = edad
        self.masa = masa

    def ficha(self):
        return f"{self.nom} | {self.edad} años | {self.masa}kg"

    def dosis(self):
        pass

    def resumen(self):
        return f"{self.ficha()} | Medicación: {self.dosis()} ml"

class Tipo1(Ser):
    def __init__(self, nom, edad, masa, dato):
        super().__init__(nom, edad, masa)
        self.dato = dato

    def dosis(self):
        return round(self.masa * 0.8, 1)

class Tipo2(Ser):
    def __init__(self, nom, edad, masa, dato):
        super().__init__(nom, edad, masa)
        self.dato = dato

    def dosis(self):
        return round(self.masa * 0.6, 1)

class Tipo3(Ser):
    def __init__(self, nom, edad, masa, dato):
        super().__init__(nom, edad, masa)
        self.dato = dato

    def dosis(self):
        return round(self.masa * 0.3, 1)

class Tipo4(Ser):
    def __init__(self, nom, edad, masa, dato):
        super().__init__(nom, edad, masa)
        self.dato = dato

    def dosis(self):
        return round(self.masa * 0.5, 1)


pac1 = Tipo1("Max", 6, 11.3, "TipoA")
pac2 = Tipo2("Luna", 4, 3.9, "TipoB")
pac3 = Tipo3("Bucky", 1, 0.2, "TipoC")
pac4 = Tipo4("Galleta", 3, 5.5, "TipoD")

for x in [pac1, pac2, pac3, pac4]:
    print(x.resumen())

