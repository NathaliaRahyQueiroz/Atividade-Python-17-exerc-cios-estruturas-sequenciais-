import math
#Declaração das variáveis 
raio: int = 0
comprimento: int = 0

#Início
raio = int(input("Digite o valor do raio da circunferência:"))
comprimento = int(2* math.pi * raio)
print ("O comprimento da circunferência é igual a:", comprimento)

#Fim