# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print("escolha uma opção: ")
print("1 - Dollar para Real")
print("2 - Real para Dollar")
opcao = int(input())
if opcao == 1:
    print("informe a cotação atual do dollar: ")
    cotacao = float(input())
    print("informe a quantidade de dólares: ")
    quantidade = float(input())
    valor_em_reais = quantidade * cotacao
    print(f"O valor em reais é R${valor_em_reais:.2f}")
elif opcao == 2:
    print("informe a cotação atual do dollar: ")
    cotacao = float(input())
    print("informe a quantidade de reais: ")
    quantidade = float(input())
    valor_em_dolares = quantidade / cotacao
    print(f"O valor em dólares é ${valor_em_dolares:.2f}")