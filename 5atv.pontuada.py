import os
os.system("cls")


operacao = input("Digite a operação (+, -, * ou /): ")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if operacao == '+':
    resultado = A + B
elif operacao == '-':
    resultado = A - B
elif operacao == '*':
    resultado = A * B
elif operacao == '/':

    if B != 0:
        resultado = A / B
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."

print("Resultado:", resultado)

print("FIM")