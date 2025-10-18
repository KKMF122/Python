nota1 = int(input("Qual é a nota do primeiro teste?: "))
nota2 = int(input("Quanl é a nota do segundo teste?: "))
nota3 = int(input("Qual é a nota do terceiro teste?: "))
nota4 = int(input("Qual é a nota do quarto teste?: "))
nota5 = int(input("Qual é a nota do quinto teste?: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print("A média foi",media)

if media > 60 :
    print("O aluno está aprovado.")
else:
    print("O alino está reprovado.")
