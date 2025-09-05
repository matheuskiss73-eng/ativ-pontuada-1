import os
os.system("cls")

kg_morango = float(input("Quantidade de morangos (Kg): "))
kg_maca = float(input("Quantidade de maçãs (Kg): "))

if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

total_kg = kg_morango + kg_maca
total_preco = preco_morango + preco_maca

if total_kg >= 10 or total_preco > 15:
    total_preco *= 0.90 

print(f"Valor a ser pago: R$ {total_preco:.2f}")
