import os
os.system ("cls")

print ("===login da conta===")

tentativas = 0

while True:
    login = (input("Digite o login: "))
    senha = (input("Digite a senha: "))

    if login == "Rian" and senha == 1234:
        print ("===Seja bem-vindo===")
        break 
    elif tentativas == 3:
        print ("Tente novamente!!")
        break
    else:
        print ("Login ou senha inválido!!")
        tentativas = tentativas+1       
    