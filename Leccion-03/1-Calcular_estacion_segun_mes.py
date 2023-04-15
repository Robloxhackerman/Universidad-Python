mes = int(input("Ingresa un mes (1 - 12): "))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = "Verano"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Otoño"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Invierno"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Primavera"
else:
    estacion = "[Fuera de rango]"

print(f'La estacion en el mes {mes} es : {estacion}.')