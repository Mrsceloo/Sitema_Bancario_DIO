menu = '''Conta Bancária: 
[1] Deposito
[2] Saque
[3] Extrato
[4] Sair
'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite um valor para Depósito: R$ "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print("Digite um valor válido!\n")

    elif opcao == "2":
        saque = float(input("Digite um Valor para saque: R$"))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Inválida! O valor de saque excede o seu saldo")

        elif excedeu_limite:
            print("Operação Inválida! O valor do saque é superior a R$ 500,00")

        elif excedeu_saques:
            print("Operação Inválida. O limite diário de saques foi excedido")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1

    elif opcao == "3":
        print("----------Saldo----------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------")
    elif opcao == "4":
        print("Até Logo")
        break

    else:
        print("Digite uma opção válida")


