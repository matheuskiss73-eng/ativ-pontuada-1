import os
os.system("cls")

vA = float(input("digite o valor a: "))
vB = float(input("digite o valor b: "))

if vA == vB:
    c = vA + vB 
    print(f"{vA}+{vB}={c}")
else:
    c = vA * vB
    print(f"{vA}*{vB}={c}")

print("fim")