import os
os.system("clear")

#Entrada
primeiro_numero = int(input("Digite o Primeiro número: "))
operador = str (input("Informe a operação desejada (+ - / *): "))
segundo_numero = int(input("Digite o Segundo número: "))

#Processamento
match operador:
    case"+":
        resultado = primeiro_numero + segundo_numero
    case"-":    
        resultado = primeiro_numero - segundo_numero
    case"*":    
        resultado = primeiro_numero * segundo_numero
    case"/":    
        resultado = primeiro_numero / segundo_numero    
    case _:
        resultado = "Operação inválida."

#Saída
print(f"\nPrimeiro Número: {primeiro_numero}")
print(f"\nOperador: {operador}")
print(f"\nSegundo Número: {segundo_numero}")
print(f"\nResultado: {resultado}")
