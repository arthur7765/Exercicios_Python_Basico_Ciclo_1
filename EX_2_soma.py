# Escreva um programa que pede ao usuário dois números e exiba no final a soma deles:
# OUTPUT ESPERADO:

# Digite um número: 10
# Digite outro número: 30
# A soma entre 10 e 30 é: 40


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

soma = 10

soma2 = 30

soma = int(input("digite um número: "))
soma2 = int(input("digite outro número: "))
soma = soma + soma2
print("a soma entre", soma, "e", soma2, "é:", soma)
10