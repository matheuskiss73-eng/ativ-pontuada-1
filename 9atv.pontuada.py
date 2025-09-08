import os
os.system("cls")



r_m = float(input("Informe sua renda mensal: R$ "))
v_e = float(input("Informe o valor do empréstimo solicitado: R$ "))
n_p = int(input("Informe o número de prestações desejado: "))


p_m = v_e / n_p


l_e = r_m * 10
l_p = r_m * 0.30


if v_e <= l_e and p_m <= l_p:
    print("\nEmpréstimo pode ser CONCEDIDO.")
    print(f"Valor da prestação: R$ {p_m:.2f}")
else:
    print("\nEmpréstimo NEGADO.")
    if v_e > l_e:
        print("O valor do empréstimo excede 10x a renda mensal.")
    if p_m > l_p:
        print("O valor da prestação excede 30% da renda mensal.")

print("FIM")