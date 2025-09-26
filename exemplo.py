import os 
os.system("cls")

maior_idade = 0
menor_idade = 99999999
print(maior_idade)
print(menor_idade)
while True:
    idade = int(input("Digite a idade: "))
    if idade > maior_idade:
            maior_idade = idade
    if idade < menor_idade:
            menor_idade = idade
    print(maior_idade)
    print(menor_idade)    