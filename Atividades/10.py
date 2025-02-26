import os
os.system("clear")

#Entrada
primeiro_numero:int(input("Digite o Primeiro número: "))
operador:float(input("Informe a operação desejada (+ - / *): "))
segundo_numeo:int(input("Digite o Segundo número"))

#Processamento
case"+":
    resultado = primeiro_numero + segundo_numero
case"-":    
    resultado = primeiro_numero - segundo_numero
case"*":    
    resultado = primeiro_numero * segundo_numero
case"/":    
    resultado = primeiro_numero / segundo_numero    
case_:
    print("Operação inválida.")

#Saída
print(f"\nPrimeiro Número: {primeiro_numero}")
print(f"\nOperador: {operador}")
print(f"\nSegundo Número: {segundo_numero}")
print(f"\nResultado: {resultado}")
