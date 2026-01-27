"""1Faça um programa que receba três notas de um aluno,
calcule a média e escreva se o aluno está aprovado (média ≥ 7),
reprovado (média < 4) ou em prova final (média entre 4 e 7)."""

saudaçao = (input("Olá, informe o seu nome     "))

print (f"Olá {saudaçao} seja bem vindo!")

nota1 = float(input("Digite a sua primeira nota      "))
nota2 = float(input(" digite a segunda nota     "))
nota3 = float(input("digite a sua terceira nota    "))

media = nota1+nota2+nota3/3

if (media >= 7):
    print ("Você está aprovado")

elif (media > 4 < 7 ):
    print (" Você está na prova final")

elif ( media < 4 ):
    print ("Você está reprovado")
    
    
    
    
    
    
    