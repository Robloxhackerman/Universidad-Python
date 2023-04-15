num = int(input("Proporcione un valor entre 1 y 3: "))

if num == 1:
    valor = "Numero UNO"
elif num == 2:
    valor = "Numero DOS"
elif num == 3:
    valor = "Numero TRES"
else:
    valor = "Fuera de rango."

print(valor)