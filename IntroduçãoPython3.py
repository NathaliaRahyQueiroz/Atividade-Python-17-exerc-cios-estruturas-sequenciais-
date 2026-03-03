#Declaração de variáveis
base: int = 0
altura: int = 0
area: int = 0

#Início
base = int(input("Digite o valor da base do triângulo:"))
altura = int(input("Digite o valor da altura do triângulo:"))
area = int((base*altura/2))
print("A área é igual a:", area)

#Fim