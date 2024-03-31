MAX_WITHDRAWALS_NUMBERS_OF_DAY = 3
MAX_WITHDRAWALS_VALUE = 500.0

balance = 0
withdrawals = 0
account_statement = []

while True:
    type = int(input("""
- - - - - - Escolha a operação - - - - - - 

 [1] Depósito
 [2] Saque
 [3] Extrato
 [4] Sair
                     
"""))

    if(type == 1):
        value = float(input('Digite o valor da depósito: '))
        if(value <= 0):
            print('\n Valor inválido.')

        else:
            balance += value
            account_statement.append(value)
            print("\n Operação realizada com sucesso!")

    elif(type == 2):
        value = float(input('Digite o valor da saque: '))
        if(value <= 0):
            print('\n Valor inválido.')

        elif((balance - value) < 0):
            print(f'\n Saldo atual de R$ {balance:.2f} insuficiente para realizar a operação.')

        elif(withdrawals >= MAX_WITHDRAWALS_NUMBERS_OF_DAY):
            print('\n Número máximo de 3 saques diários já atingido.')

        elif(value > MAX_WITHDRAWALS_VALUE):
            print(f'\n Saque máximo por operação de R$ {MAX_WITHDRAWALS_VALUE:.2f}')

        else:
            balance -= value
            account_statement.append(value * -1)
            withdrawals += 1
            print("\n Operação realizada com sucesso!")
            
    elif(type == 3):
        if(len(account_statement) == 0):
            print("** Não existem movimentações no período. ** \n")
            print(f"\n Saldo atual de R$ {balance:.2f}  ")

        else:
            print(" *** Extrato do período *** \n")

            for value in account_statement:
                print(f"  R$ {value:.2f}" if (value > 0) else f"- R$ {(value *-1):.2f}")

            print(f"\n Saldo atual de R$ {balance:.2f}  \n")
    
    elif(type == 4):
        print('Até logo! \n')
        break

    else:
        print('Operação inválida. Selecione uma das opções do menu \n')





        

    