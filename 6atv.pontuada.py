import os
os.system("cls")

nome = input("digite seu nome: ")

n1 = float(input("digite o primeira nota : "))
n2 = float(input("digite o segunda nota : "))

media = (n1 + n2) / 2

if media >=6 :
        print (f"a sua média é {media}: VOCÊ FOI APROVADO  PARABÉNS!!! {nome}")

elif media >= 4.1 < 5.9:
    print (f"a sua média é {media}; VOCÊ ESTÁ DE RECUPERAÇÃO")

elif media >= 4:
    print (f"a sua média é {media}; VOÊ FOI REPROVADO")



print(".") 