edad = int(input("Introduce tu edad: "))

veintes = edad >= 20 and edad < 30
treintas = edad >= 30 and edad < 40

if veintes or treintas:
    print("Estas dentro del rango.")
else:
    print("No estas dentro del rango.")