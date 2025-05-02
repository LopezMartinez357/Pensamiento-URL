class Registro:
    def __init__(self, n, e, idn):
        self.n = n
        self.e = e
        self.idn = idn

    def ver(self):
        return f"{self.n} - {self.e} años - ID: {self.idn}"

class TipoA(Registro):
    def __init__(self, n, e, idn, grado, cod):
        super().__init__(n, e, idn)
        self.grado = grado
        self.cod = cod

    def ver(self):
        return f"{super().ver()} - {self.grado} ({self.cod})"

class TipoB(Registro):
    def __init__(self, n, e, idn, area, clave):
        super().__init__(n, e, idn)
        self.area = area
        self.clave = clave

    def ver(self):
        return f"{super().ver()} - {self.area} / {self.clave}"

class TipoC(Registro):
    def __init__(self, n, e, idn, rol, ext):
        super().__init__(n, e, idn)
        self.rol = rol
        self.ext = ext

    def ver(self):
        return f"{super().ver()} - {self.rol} @ {self.ext}"


x1 = TipoA("Mario", 19, "001", "Computación", "E045")
x2 = TipoB("Juan", 42, "002", "Física", "P888")
x3 = TipoC("Daniel", 37, "003", "Archivo", "112")
for y in [x1, x2, x3]:
    print(y.ver())
