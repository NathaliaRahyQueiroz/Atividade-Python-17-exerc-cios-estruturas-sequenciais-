#Declaração das variáveis 
velocidade: int = 0
tempo: float = 0.0
espaço: int = 0
litrosGastos: float = 0.0

#Início
velocidade = int(input("Digite a velocidade média do automóvel em km/h:"))
tempo = float(input("Digite o tempo para realizar o percuso em horas:"))
espaço = velocidade * tempo
litrosGastos = espaço / 12
print ("A quantidade de litros gastos no percurso foi de:", litrosGastos)

#Fim