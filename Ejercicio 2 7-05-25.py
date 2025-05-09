import math
class OperacionCientifica:
    def calcular(self, valor):
        pass

class RaizCuadrada(OperacionCientifica):
    def calcular(self, valor):
        if valor < 0:
            print("Error: no se puede sacar la raíz de un número negativo.")
            return None
        return math.sqrt(valor)

class Potencia(OperacionCientifica):
    def calcular(self, valor):
        base, exponente = valor
        return base ** exponente

class Logaritmo(OperacionCientifica):
    def calcular(self, valor):
        if valor <= 0:
            print("Error: no se puede calcular logaritmo de un número no positivo.")
            return None
        return math.log10(valor)

class Factorial(OperacionCientifica):
    def calcular(self, valor):
        if valor < 0 or int(valor) != valor:
            print("Error: el factorial solo funciona con enteros no negativos.")
            return None
        return math.factorial(int(valor))


print("Calculadora Científica Simple")
print("1. Raíz Cuadrada")
print("2. Potencia")
print("3. Logaritmo")
print("4. Factorial")

opcion = input("Elige una opción (1-4): ")

if opcion == "1":
    num = float(input("Ingresa un número: "))
    op = RaizCuadrada()
    print("Resultado:", op.calcular(num))

elif opcion == "2":
    base = float(input("Base: "))
    exponente = float(input("Exponente: "))
    op = Potencia()
    print("Resultado:", op.calcular((base, exponente)))

elif opcion == "3":
    num = float(input("Ingresa un número: "))
    op = Logaritmo()
    print("Resultado:", op.calcular(num))

elif opcion == "4":
    num = float(input("Ingresa un número entero: "))
    op = Factorial()
    print("Resultado:", op.calcular(num))

else:
    print("Opción inválida.")
