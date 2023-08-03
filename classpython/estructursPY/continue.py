#El continue permite continuar (valga la redundancia) el codigo sin que se vea afectado por alguna condicion
for i in range(10):
    if i%2==0:
        print(f"El {i} es par")
    else:
        continue #Si el valor es impar, entonces no pasa nada, solo continua el ciclo y este no se ve afectado.
"""
La verdad no le encuejtro nada de utilidad al continue, pues si omitimos es linea el ciclo continuara funcionando igual
"""
print("-------------------")
for i in range(10):
    if i%2==0:
        print(f"El {i} es par")
