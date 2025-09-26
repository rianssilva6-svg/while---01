import os
os.system ("cls")

pares = 0
impares = 0

while True:
 numero = int(input("Digite o número: "))
 
 if numero == 0:
   break  
 if int (numero) % 2 == 0:
  pares += 1 
  media = pares / numero
 else:
  impares += 1

print (f"pares: {pares}")
print (f"impares: {impares}")
print (f"media dos pares: {media}")
