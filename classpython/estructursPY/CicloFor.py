#Este archivo me ayudará a recordar todas las estructuras de python que se me pudieron haber olvidado.
"""
ESTRUCTURAS DE PYTHON
"""
# FOR para la tabla del 3
for i in range(10):
    print(f"{i+1} * 3 = {i*3}")


# FOR con la funcion enumerate
objects = ["house", "car", "cycle"]
for i, fruit in enumerate(objects):
    print("Psition ", i, "  elemenet ", objects)

# FOR con "_" para ignorar valor de lo que haya en una lista
objects = ["house", "car", "cycle"]
for _ in objects:
    print("Estoy ignorando el valor de la variable: ", _)
    """
    Aunque la verdad no se que fin tiene, ya que si corremos ese ejercicio,
    podemos ver que va a imprimir el valor que tome "_" así que podemos con
    "for i in objects: print("imprimir cualquier cosa")" y asi ignorar todos los valoresque tome "i"
    """

# FOR para iterar dos (o más) listas al mismo tiempo con zip()
objects = ["house", "car", "cycle"]
elements = ["chair", "horn", "wheel"]
for i,j in zip(objects, elements):
    print(f" Esto: {i} tiene esto: {j}")
    