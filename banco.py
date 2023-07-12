print("Olá, bem-vindo ao banco DIO!")


saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    operacao = int(input("Digite o número correspondente à operação desejada:\n1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Sair\n"))

    if operacao == 1:
        deposito = float(input("Digite o valor desejado:\n"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito de {saldo:.2f} reais."
        else:
            print("Error!")
    elif operacao == 2:
        saque = float(input("Digite o valor desejado:\n"))
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Você excedeo o limite de saque.")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque de {saldo:.2f} reais."
            numero_saques += 1
        else:
            print("Error!")
    
    elif operacao == 3:
        print("=======Extrato======")
        print("Não foram realizadas operações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    elif operacao == 4:
        break
    else:
        print("Error")
        break
    
   