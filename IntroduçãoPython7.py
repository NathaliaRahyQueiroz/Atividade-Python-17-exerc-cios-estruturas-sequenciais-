#Declaração das variáveis 
comprimento: int = 0
largura: int = 0 
altura: int = 0
volume: int = 0

#Início
comprimento = int(input("Digite o valor do comprimento do paralelepípedo:"))
largura = int(input("Digite o valor da largura do paralelepípedo:"))
altura = int(input("Digite o valor da altura do paralelepípedo:"))
volume = int(comprimento*altura*largura)
print("O volume do paralelepípedo é igual:", volume)

#Fim