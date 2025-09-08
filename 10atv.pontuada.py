import os
os.system("cls")

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ").upper()

preco_a = 3.79
preco_g = 6.59

if tipo == "A":
    preco_b = litros * preco_a
    if litros <= 25:
        desconto = 0.10
    else:
        desconto = 0.20
elif tipo == "G":
    preco_b = litros * preco_g
    if litros <= 25:
        desconto = 0.15
    else:
        desconto = 0.30
else:
    print("Tipo de combustível inválido.")
    exit()  


valor_d = preco_b * desconto
valor_f = preco_b - valor_d


print(f"Valor a ser pago: R$ {valor_f:.2f}")

print("FIM")