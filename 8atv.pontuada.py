import os
os.system("cls")

print("""
produto \t CD's  \t\t valor
      
 Verde \t\t CD Verde\t R$ 10,00
      
 Azul \t\t CD Azul  \t R$ 20,00
      
 Amarelo \t CD Amarelo \t R$ 30,00
      
 Vermelho \t CD Vermelho \t R$ 40,00
""")

produto =str(input("digite a cor relacionado ao produto: "))

match produto:
    case "Verde":
        print("CD Verde R$ 10,00")
    case "Azul":
        print("CD Azul R$ 20,00")
    case "Amarelo":
        print("CD Amarelo R$ 30,00")
    case "Vermelho":
        print("CD Vermelho R$ 40,00")
    case _:
        print("Opção fora do menu.")

print("OBRIGADO PELA ESCOLHA")  