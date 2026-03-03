#Declaração das variáveis
deposito: float = 0
aplicaçao: float = 0
#Início
deposito = float(input("Digite o valor do depósito:"))
aplicaçao = float(deposito *  1.013)
print("O valor da aplicação após 1 mês com rendimento de 1.3% ao mês é de:", aplicaçao)
#Fim