#Declaração das variáveis 
anoDeNascimento: int = 0
anoAtual: int = 0
idade: int = 0
idadeFutura: int = 0

#Início
anoDeNascimento = int(input("Digite o seu ano de nascimento:"))
anoAtual = int(input("Digite o ano atual:"))
idade = int(anoAtual - anoDeNascimento)
print("Sua idade atual é", idade, "anos")
idadeFutura = int(idade + 17)
print("Sua idade daqui 17 anos será de:", idadeFutura, "anos")

#Fim