import math
#Declaração das variáveis
coeficienteA: int = 0
coeficienteB: int= 0
coeficienteC: int = 0
delta: int = 0
raiz1: int =0
raiz2: int = 0

#Início
coeficienteA = int(input("Digite o valor do coeficiente A:"))
coeficienteB = int(input("Digite o valor do coeficiente B:"))
coeficienteC = int(input("Digite o valor do coeficiente C:"))
delta = int((coeficienteB**2) - (4 * coeficienteA * coeficienteC))
raiz1 = (((-1) * coeficienteB) + (math.sqrt(delta))) / (2*coeficienteA)
raiz2 = (((-1) * coeficienteB) - (math.sqrt(delta))) / (2*coeficienteA)
print("Os valores das raizes são:", raiz1, "e", raiz2)

#Fim