import os
os.system("cls")

nome = input("Digite o seu nome: ")
sx = input("Digite seu sexo (M/F): ")
ec = input("Digite seu estado civil : ")

tc = None

if sx == "F"  and ec == "casada":
    tc = int(input("Digite seu tempo de casada (em anos): "))

print("\n=== Dados do usuario===")
print(f"nome: {nome}")
print(f"sexo: {sx}")
print(f"estado civil: {ec}")



if tc is not None:
    print(f"tempo de casada: {tc} anos")

print("FIM")