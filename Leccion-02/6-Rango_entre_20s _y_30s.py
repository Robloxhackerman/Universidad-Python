edad = int(input("Introduce tu edad: "))

veintes = edad >= 20 and edad < 30
treintas = edad >= 30 and edad < 40

if veintes or treintas:
    print("Dentro del rango de los 20's o 30's")

    if veintes:
        print("Dentro del rango de los 20's")
    elif treintas:
        print("Dentro del rango de los 30's")
else:
    print("No estas dentro del rango.")