#Declaração das variáveis 
anguloA: int = 0 
anguloB: int = 0 
anguloC: int = 0

#Início
anguloA = int(input("Digite o valor do ângulo A do triângulo:"))
anguloB = int(input("Digite o valor do ângulo B do triângulo:"))
anguloC = int(180 - anguloA - anguloB)
print ("O valor do ângulo C é de:", anguloC)