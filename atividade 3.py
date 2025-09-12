import os
os.system ("cls")

print ("===login da conta===")

while True:
    login = (input("Digite o login: "))
    senha = int(input("Digite a senha: "))

    if login == "Rian" and senha == 1234:
        print ("===Seja bem-vindo===")
    else:
        print ("Login ou senha inválido!!")
        break