import os
os.system("cls || clear")

def calcular_imc (peso, altura):
    return peso / (altura * altura)

def situacao (imc):
    
    if imc >= 40:
        classificacao = "Obesidade grau III"
        recomendacao = "Buscar assistência médica imediatamente" 
    elif imc >= 35:
        classificacao = "Obesidade grau II"
        recomendacao = "Consulte um médico para avaliação e orientação "
    elif imc >= 30:
        classificacao = "Obesidade grau I"
        recomendacao = "Procure orientação de um profissional de saúde"
    elif imc >= 25:
        classificacao = "Sobrepeso"
        recomendacao = "Considere uma dieta balanceada e ativicdade física"
    elif imc >= 18.5:
        classificacao = "Peso normal"
        recomendacao = "Mantenha hábitos saudáveis"
    else: 
        classificacao = "Abaixo de peso"
peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))

imc = calcular_imc(peso, altura)
(classicacao, recomendacao) = situacao
