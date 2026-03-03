#Declaração das variáveis 
horasTrabalhadas: int = 0
valorPorHora: int = 0
percentualDesconto: float = 0.0
dependentes: int = 0 
salarioBruto: int = 0
salarioLiquido: int  = 0
salario: int = 0

#Início
horasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas:"))
valorPorHora = int(input("Digite o valor recebido por hora:"))
percentualDesconto = float(input("Digite o percentual de desconto:"))
dependentes = int(input("Digite o número de dependentes:"))
salarioBruto = horasTrabalhadas * valorPorHora 
salarioLiquido = salarioBruto - (salarioBruto * (percentualDesconto/100))
salario = salarioLiquido + (100 * dependentes)
print ("O valor do salário é de:", salario)

#Fim