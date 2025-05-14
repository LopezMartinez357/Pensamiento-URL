dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
niveles_azucar = [130, 160, 95, 175, 160]
niveles_sal = [2000, 2400, 1800, 2400, 2700]
presion_sistolica = [115, 130, 110, 125, 175]
presion_diastolica = [75, 78, 70, 77, 95]


total_azucar = 0
total_sal = 0
total_sistolica = 0
total_diastolica = 0

print("RESULTADOS SEMANALES\n")

for i in range(len(dias)):
    print(f"Día: {dias[i]}")
    
    azucar = niveles_azucar[i]
    sal = niveles_sal[i]
    sistolica = presion_sistolica[i]
    diastolica = presion_diastolica[i]
    

    total_azucar += azucar
    total_sal += sal
    total_sistolica += sistolica
    total_diastolica += diastolica

    if 70 <= azucar <= 140:
        print(f"  Azúcar: {azucar} mg/dL (Normal)")
    else:
        print(f"  Azúcar: {azucar} mg/dL (Fuera de rango)")

    if sal <= 2300:
        print(f"  Sal: {sal} mg (Aceptable)")
    else:
        print(f"  Sal: {sal} mg (Exceso de consumo)")

   
    if sistolica < 120 and diastolica < 80:
        clasificacion = "Presión normal"
    elif 120 <= sistolica <= 129 and diastolica < 80:
        clasificacion = "Presión elevada"
    elif 130 <= sistolica <= 139 or 80 <= diastolica <= 89:
        clasificacion = "Hipertensión Etapa 1"
    elif sistolica >= 140 or diastolica >= 90:
        clasificacion = "Hipertensión Etapa 2"
    else:
        clasificacion = "No Aplicable"
    
    print(f"  Presión: {sistolica}/{diastolica} mmHg ({clasificacion})\n")


promedio_azucar = total_azucar / len(dias)
promedio_sal = total_sal / len(dias)
promedio_sistolica = total_sistolica / len(dias)
promedio_diastolica = total_diastolica / len(dias)

print("PROMEDIOS DE LA SEMANA\n")
print(f"Promedio azúcar: {promedio_azucar:.2f} mg/dL")
print(f"Promedio sal: {promedio_sal:.2f} mg")
print(f"Promedio presión: {promedio_sistolica:.2f}/{promedio_diastolica:.2f} mmHg\n")

print("ALERTAS SEMANALES")
if not (70 <= promedio_azucar <= 140):
    print("Promedio de azúcar fuera de lo normal")
if promedio_sal > 2300:
    print("Promedio de sal supera lo recomendado")
if promedio_sistolica >= 140 or promedio_diastolica >= 90:
    print("Presión promedio indica Hipertensión Etapa 2")
elif 130 <= promedio_sistolica <= 139 or 80 <= promedio_diastolica <= 89:
    print("Presión promedio indica Hipertensión Etapa 1")
elif 120 <= promedio_sistolica <= 129 and promedio_diastolica < 80:
    print("Presión promedio elevada")
elif promedio_sistolica < 120 and promedio_diastolica < 80:
    print("Presión promedio dentro del rango normal")
