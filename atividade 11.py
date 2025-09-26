import os
os.system ("cls")

quant_familia = 0
contar_familia = 0
contar_filhos = 0
soma = 0
menor_salario = 9999999
maior_salario = 0
total_salario = 0
total_filhos = 0

#Desenvolvimento
while True:
 print ("""
Código | Descrição
    1  | Adicionar familia
    2  | Exibir dados e sair""")

 escolha = int(input("Digite a ação que deseja: "))

#Registro 
 match escolha:
  case 1:
    quant_filhos = int(input("Quantidade de filhos: "))
    contar_familia += 1
#salario       
    salario = float(input("Digite o salário: "))    

    total_salario += salario
    total_filhos += quant_filhos

    if salario > maior_salario:
      maior_salario = salario
    if salario < menor_salario:
      menor_salario = salario
      os.system ("cls")

#Exibição e saída
  case 2:
    media_salario = total_salario / contar_familia
    media_filhos = total_filhos / quant_familia
    print (f"Quantidade de familia com filhos: {contar_filhos: .2f}")
    print (f"Maior salario {maior_salario: .2f} menor salario {menor_salario: .2f}")
    print (f"Média do salario: {media_salario: .2f}")
    print (f"Média dos filhos: {media_filhos: .2f}")
    break 
os.system ("cls")

    


