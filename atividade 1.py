import os
os.system ("cls")

print ("===Notas===")

while True:
    numero = float(input("Digite a nota do aluno: "))
    if numero > 10 or numero < 0:
        print ("=== Escreva um algoritmo que solicite ao usuario a nota de um aluno! ===")
        break