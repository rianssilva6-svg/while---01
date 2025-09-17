
def mostrar_menu():
 print ("===RESTAURANTE===")
 print ("1 - Picanha R$25,00")
 print ("2 - Lasanha R$20,00")
 print ("3 - Strogonoff R$18,00")
 print ("4 - Bife Acebolado R$15,00")
 print ("5 - Pão com ovo R$5,00")

print ("\n")

escolha = int(input("Digite o número do prato: "))
def obter_prato():

     while True:
      if escolha == 1:
       print ("seu prato foi Picanha, o valor é R$25,00")
       break
      if escolha == 2:
       print ("Seu prato foi Lasanha, o valor é R$20,00")
       break
      if escolha == 3:
       print ("Seu prato foi strogonoff, o valor é R$18,00")
       break 
      if escolha == 4:
       print ("Seu prato foi bife acebolado, o valor é R$15,00")
       break     
      if escolha == 5:
       print ("Seu prato foi pão com ovo, seu valor é R$5,00") 
       break 
      else:
        return escolha
print("Por favor, digite um número válido!")
    