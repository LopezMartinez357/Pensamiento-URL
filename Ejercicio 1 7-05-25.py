from abc import ABC, abstractmethod

class Experimento(ABC):
    @abstractmethod
    def realizar_experimento(self):
        pass
class Caida_libre(Experimento):
    def __init__(self, altura, gravedad):
        self.altura = altura
        self.gravedad = gravedad
    def realizar_experimento(self):
        if self.altura < 0:
            print("La altura no puede ser negativa")
        if self.gravedad == 0:
            print("La gravedad no puede ser 0")
    
        dato = 2* self.altura / self.gravedad
        tiempo = dato ** 0.5
        return tiempo
try:
    altura = float(input("Ingresa la altura en metros: "))
    gravedad = float(input("Ingresa la gravedad ne m/s^2: "))
    intento1 = Caida_libre (altura, gravedad)
    tiempo_caida = intento1.realizar_experimento()
    print(f"El tiempo de caída es: {tiempo_caida:.2f} segundos")
except ValueError as e:
    print(f"Error: {e}")

    

