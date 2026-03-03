#Declaração de variáveis 
salario: int = 0
reajuste: float = 0
valorReajustado: int=0

#Início
salario = int(input("Digite o valor do salário"))
reajuste = 1.15
valorReajustado = int(salario * reajuste)
print ("O salário reajustado é igual a", valorReajustado)

#Fim