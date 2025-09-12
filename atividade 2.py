import os 
os.system ("cls")

print ("===média do aluno===")

while True:
    n1 = float(input("Digite a primeira nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))
    media = (n1 + n2) / 2
    
    print ("\n")
    print (f"sua média foi {media}")

    if media > 10 or media < 0:
        print ("Digite as notas do aluno corretamente!")
    else:
        break    