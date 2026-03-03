#Declaração das variáveis 
import math
catetoB: int = 0
catetoC: int = 0
hipotenusa: int = 0

#Início
catetoB = int(input("Digite o valor do cateto B do triângulo retângulo:"))
catetoC = int(input("Digite o valor do cateto C do triângulo retângulo:"))
hipotenusa = int(math.sqrt(catetoB**2 + catetoC**2))
print("A hipotenusa do triângulo retângulo é igual a:", hipotenusa)

#Fim