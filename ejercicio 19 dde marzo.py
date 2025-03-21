def cajero_automatico():
    saldo = 3000
    intentos = 0
    max_intentos = 3
    salir = False
    
    while saldo > 0 and not salir:
        print(f"Saldo actual: Q{saldo}")
        retiro = input("Ingrese monto a retirar: ")
        
        if retiro.isdigit():
            retiro = int(retiro)
            
            if retiro == 0:
                print("Operación cancelada. Adiós.")
                salir = True
            elif retiro > saldo:
                intentos += 1
                if intentos >= max_intentos:
                    print("Ha excedido el número de intentos. Operación cancelada.")
                    salir = True
                else:
                    print(f"Saldo insuficiente. Intentos restantes: {max_intentos - intentos}")
            else:
                saldo -= retiro
                print(f"Retiro exitoso. Nuevo saldo: Q{saldo}")
                intentos = 0
                
                if saldo == 0:
                    print("Retiro exitoso. Saldo agotado. Adiós.")
                    salir = True
        else:
            print("Entrada no válida. Ingrese un número entero.")

cajero_automatico()
