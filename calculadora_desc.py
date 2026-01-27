


"""Calculadora de descontoPeça ao USUÁRIO digitar o valor de uma compra e a forma
de pagamento:
À vista: 10% de desconto
Cartão: preço normal
Parcelado: 10% de acréscimo
O programa deve mostrar o valor final a ser pago."""




("------------- CALCULADORA DE DESCONTO -------------")



saudaçao = (input("Olá, informe o seu nome     "))
print (f"Olá {saudaçao} seja bem vindo!")


valor = float(input("Digite o valor de uma compra     "))

print ("FORMAS DE PAGAMENTO")


print (f"Digite 1 se for a vista (com 10% de desconto)")
print ("Digite 2 se for cartao (preço normal)")
print (f"Didite 3 se for parcelado (10% de acrescimo)")


pagamento = int(input("Digite o numero que indica a forma de pagamento     "))



calculo10 = (valor * 0.10)

total1 = valor - calculo10

total3 = valor + calculo10



if ( pagamento == 1 ):
    print (f"sua compra sai por {total1:.2f}")
    

elif (pagamento == 2 ):
    print (f"sua compra sai por {valor:.2f}")
    
    
elif (pagamento == 3 ):
    print (f"sua compra sai por {total3:.2f}")



 









"""Um restaurante possui mesas com 4 lugares cada. Escreva um programa que solicite ao usuário a quantidade de pessoas que vão ao jantar e 
calcule o número mínimo de mesas necessárias para acomodar todos, sem deixar ninguém em pé."""







































































































































