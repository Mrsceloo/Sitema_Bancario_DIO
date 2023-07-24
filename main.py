menu = '''Conta Bancária: 
[1] Deposito
[2] Saque
[3] Extrato
[4] Sair
'''
saldo = 6000
limite = 500
extrato = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito")

    elif opcao == "2":
        print("Saque")

    elif opcao == "3":
        print("Extrato")

    elif opcao == "4":
        print("Até Logo")
        break

    else:
        print("Digite uma opção válida")

