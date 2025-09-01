menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
contador_saques = 0
LIMITE_SAQUES = 3

while True:
    escolha = input(menu)

    if escolha == "d":
        deposito = float(input("Digite o valor que deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito realizado: R$ {deposito:.2f}\n"
        else:
            print("Valor inválido! Depósito não realizado.")

    elif escolha == "s":
        saque = float(input("Digite o valor que deseja sacar: "))

        if saque <= 0:
            print("Valor inválido! Saque não realizado.")
        elif saque > saldo:
            print("Saldo insuficiente!")
        elif saque > limite:
            print("Valor excede o limite de saque!")
        elif contador_saques >= LIMITE_SAQUES:
            print("Número máximo de saques atingido!")
        else:
            saldo -= saque
            extrato += f"Saque realizado: R$ {saque:.2f}\n"
            contador_saques += 1

    elif escolha == "e":
        print("\n=========== EXTRATO ===========")
        if extrato:
            print(extrato)
        else:
            print("Nenhuma movimentação realizada.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("================================")

    elif escolha == "q":
        print("Saindo... Até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")
