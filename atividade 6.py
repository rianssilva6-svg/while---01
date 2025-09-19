total = 0
while True:
    print("\n=== RESTAURANTE ===")
    print("1 - Picanha R$25,00")
    print("2 - Lasanha R$20,00")
    print("3 - Strogonoff R$18,00")
    print("4 - Bife Acebolado R$15,00")
    print("5 - Pão com ovo R$5,00")

    pedido = int(input("Digite o número do prato: "))
    continuar = 0
    match pedido:
        case 1:
            print ("Seu prato foi Picanha, seu valor é R$25,00")
            continuar = input("Deseja solicitar mais um prato? s ou n? ")
            total = total + 25
            if continuar == "s":
                print ("Aguarde")
            elif continuar == "n":
                print ("Encerrando")
                break    
        case 2:
            print ("Seu prato foi Lasanha, seu valor é R$20,00")
            continuar = input("Deseja solicitar mais um prato? s ou n? ")
            total = total + 20
            if continuar == "s":
                print ("Aguarde")
            elif continuar == "n":
                print ("Encerrando")
                break    
        case 3:
            print ("Seu prato foi Strogonoff, seu valor é R$18,00")
            continuar = input("Deseja solicitar mais um prato? s ou n? ")
            total = total + 18
            if continuar == "s":
                print ("Aguarde")
            elif continuar == "n":
                print ("Encerrando")
                break    
        case 4:
            print ("Seu prato foi Bife Acebolado, seu valor é R$15,00")
            continuar = input("Deseja solicitar mais um prato? s ou n? ")
            total = total + 15
            if continuar == "s":
                print ("Aguarde")
            elif continuar == "n":
                print ("Encerrando")
                break    
        case 5:
            print ("Seu prato foi Pão com ovo, seu valor é R$5,00")
            continuar = input("Deseja solicitar mais um prato? s ou n? ")
            total = total + 5
            if continuar == "s":
                print ("Aguarde")
            elif continuar == "n":
                print ("Encerrando")
                break    
        case _:
            print ("Digite o valor do prato corretamente!!")    

print (f"O valor total dos pedidos foi R${total: .2f}")