edad = int(input("Proporcione su edad: "))

mensaje = None

if 0 <= edad < 10:
    mensaje = "La infancia es increíble..."
elif 10 <= edad < 20:
    mensaje = "Muchos cambios y mucho estudio..."
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo..."
else:
    mensaje = "Etapa de vida desconocida :("

print(mensaje)