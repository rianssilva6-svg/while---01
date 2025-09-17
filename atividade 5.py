import os
os.system ("cls")

nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
n3 = float(input("Digite a terceira nota do aluno: "))

media = (n1 + n2 + n3) / 3

while True:
    if media > 7:
        print (f"Parabens, vc esta aprovado, sua média foi {media}")
        break
    elif media >= 5 and 6.9:
        print (f"Voce esta de recuperação, sua média foi {media}")
        break
    else:
        print (f"Você esta reprovado, sua media foi {media}")        
        break