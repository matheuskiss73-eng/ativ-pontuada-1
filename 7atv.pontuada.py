import os
os.system("cls")

n = input("Digite a descrição do produto: ")
q = int(input("Digite a quantidade adquirida: "))
p = float(input("Digite o preço unitário (R$): "))

total = q * p


if q <= 5:
    d_p = 2
elif q <= 10:
    d_p = 3
else:
    d_p = 5

d = (d_p / 100) * total
t_p = total - d


print("\n--- RESUMO DA COMPRA ---")
print(f"Produto: {n}")
print(f"Quantidade: {q}")
print(f"Preço unitário: R$ {p:.2f}")
print(f"Total sem desconto: R$ {total:.2f}")
print(f"Desconto aplicado: {d_p}% (R$ {d:.2f})")
print(f"Total a pagar: R$ {t_p:.2f}")

print("FIM")