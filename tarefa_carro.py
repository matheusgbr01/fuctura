



print ("olá, mundo!")

marca = input ("Qual é a marca do carro?   ")
modelo = input ("Qual é o modelo do carro?    ")
cor = input ("Qual é a cor do carro?   ")
ano = int ( input ("Qual é o ano do carro?"))
valor = int ( input("Qual valor que foi comprado o carro? "))

#print (f"a marca do seu carro é: {marca} ; a cor  dele é {cor} ; o ano do carro é {ano} e o valor do seu carro é R${valor:.2f}")
#print (f"a marca do seu carro é: {marca} ; o modelo do carro é:{modelo} ; a cor  dele é {cor} ; o ano do carro é {ano} o valor do seu carro é R${valor:.2f}")


capital = (valor) # aqui eu soube a captal; a taxa eu coloquei em decimais; o tempo perguntei; e dps so multipliquei o resto da taxa pelo tempo que ele pretende vender
taxa = 0.10 
tempo = int(input("Em quantos anos você pretende  vender o carro"))

venda = 0.90**tempo

resultado = venda*capital



print (f"a marca do seu carro é: {marca} ; o modelo do carro é:{modelo} ; a cor  dele é {cor} ; o ano do carro é {ano} o valor do seu carro é R${valor:.2f}")
print (f"E  seu carro vai ser vendido por {resultado:.2f} com a taxa de 10% de desvalorização ao ano")


viagem = float(input("Você vai fazer uma viagem, diga quantos km você vai andar"))
litro = float( input("Quantos km o seu carro percorre usando apenas 1 litro de combustivel?"))



litragem = viagem/litro

print (f"{litragem:.2f}")

gasolina = 6.50
gasto = gasolina*litragem


print (f"Para você fazer essa viagem você vai gastar R${gasto:.2f} de combustivel com a gasolina saindo a 6.50")

''' aqui eu descubri os km  que ele vai prescisar pra fazer a viagem ; dps eu descubri quantos km ele faz por litros e dividi os km's pelos km's por litro '''
































































































































































