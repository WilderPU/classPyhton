#El ciclo while puede parecerse a un ciclo for, con la unica diferencia que el ciclo while lo puede hacer segun una condicion, en cambio el ciclo for tiene que hacerlo segun la longitud de una lista.
cont=1
# While para hacer la tabla del 3
while cont<10:
 print(f"{cont} * 3 = {cont * 3}")
 cont+=1

# While que repite la misma pregunta hasta que sea verdadera la respuesta
while True:
 answer = int(input("¿Cuánto es 1+1?"))
 if answer == 2:
  print("Eso es correcto")
  break #Este sirve para para el ciclo cuando la condicion "answer == 2" sea cierta.
 else:
  print("Incorrecto, vuleva a intentarlo")
  #En caso contrario, tendra que responder otra vez la pregunta hasta que de la respuesta correcta

# While como contador con ayuda de la libreria time
import time
userTime  = int(input("Ingrese los segundos que desee esperar"))
clockTime = 1

while clockTime != userTime+1:
 print(clockTime)
 time.sleep(1)
 clockTime+=1