import os
os.system ("cls")

contar = 0
soma = 0

while True:
    numero = int(input("Digite o número: "))
    if numero >= 0:
     contar += 1
     soma += numero
     media = soma / contar
    if numero < 0:
        break

print (f"Quantidade de notas: {contar}")    
print (f"Total: {soma}")    
print (f"Sua média: {media}")    
