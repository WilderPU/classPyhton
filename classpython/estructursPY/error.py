"""
Los errores son algo común, y hay que saber manejarlos cuando estos ocurren.
Podemos evitar errores cuando nuestro codigo se este ejecutando usando condiciones para evitar eso,
o exponiendo el error de manera evidente y poder manejarlo de otra manera
"""
# Error al introducir letras en vez de numeros

text = "hello"
try:
    number = int(text)
except ValueError:
    print("no puedes convertir una cadena de caracteres en números")