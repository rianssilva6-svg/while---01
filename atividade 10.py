import os
os.system ("cls")

#As variáveis
contar_m = 0
contar_f = 0
maior_idade = 0
menor_idade = 99999999
soma = 0
alto_salario = 0
total = 0

#Desenvolvimento
while True:
 print ("""
Código | Descrição
    1  | Adicionar pessoas
    2  | Exibir dados 
    3  | sair""")

 escolha = int(input("Digite a ação que deseja: "))

#Registro 
 match escolha:
    case 1:
        idade = int(input("Digite a idade: "))
        if idade > maior_idade:
            maior_idade = idade
        if idade < menor_idade:
            menor_idade = idade
        sexo = input("Digite o sexo (M ou F)").upper()      
        if sexo == "M":
            contar_m += 1
        elif sexo == "F":
            contar_f += 1
#salarial
        salario = float(input("Digite o salário: "))
        soma += salario 
        if salario >= 5000 and sexo == "F":
            alto_salario += 1
            os.system ("cls")

#Exibição de dados
    case 2:
        total = contar_f + contar_m
        media = soma/total 
        print(f"Média salarial: {media: .2f}")
        print(f"Maior idade: {maior_idade}\n Menor idade: {menor_idade}")
        print(f"Quantidade de mulheres com salário alto: {alto_salario}")
        break

#Saida
    case 3:
         os.system ("cls")
         print ("Encerrando...")
         break

#Finalização
    case _:
        print ("Valor inválido")
        error = input("Digite qualquer coisa para retornar")
        os.system ("cls")      


         