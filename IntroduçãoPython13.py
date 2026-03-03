#Declaração das variáveis 
quantidade: int = 0
quantidadeEmGramas: int = 0
dias: int = 0

#Início
quantidade = int(input("Digite a quantidade de alimento em quilograma:"))
quantidadeEmGramas = quantidade * 1000
dias = int(quantidadeEmGramas / 50)
print ("O alimento durará por:", dias, "dias")

#Fim