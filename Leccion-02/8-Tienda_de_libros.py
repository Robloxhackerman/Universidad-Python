print("Porporciona los datos del libro...")
print("")

nombre = input("Ingrese el nombre del libro: ")
id = int(input("Ingrse el id del libro: "))
precio = float(input("Ingrese el precio: $"))
envio = input("Engio gratis? (True/False)")

if envio == 'True':
    envio = True
elif envio == 'False':
    envio == False
else:
    print("Los valores de envio deben ser True o False")

print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envio gratis: {envio}
''')