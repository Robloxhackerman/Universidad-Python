"""
Instrucciones de tareas:

Solicitar al usuario dos valores, y determinar cual número es el mayor

numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser identica a la que sigue):
Proporciona el primer valor:
Proporciona el segundo valor:
El numero mayor es:<numeroMayor>
"""

numero1 = int(input("Proporciona el primer valor: "))
numero2 = int(input("Proporciona el segundo valor: "))

if numero1 > numero2:
    print(f'El numero mayor es: {numero1}')
elif numero2 > numero1:
    print(f'El numero mayor es: {numero2}')