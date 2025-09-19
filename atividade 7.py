import os
os.system ("cls")

total = 0
contar = 0

while True:
   nome = input("Digite o nome do aluno: ")
   nota = int(input("Digite a nota do aluno: "))
   

   match nota:
      case nota:
         print(f"Sua nota foi {nota} ")
         continuar = input("Deseja tentar de novo? S ou N? ").upper()
         contar = contar + 1
         total = nota + total
         media = total / contar
         if continuar == "S":
            print ("Tente de novo")
         elif continuar == "N":
            print ("Encerrando")
            break   

print (f"Sua nota foi {total}")         
print (f"Sua média foi {media}")         