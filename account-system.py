MAX_WITHDRAWALS_NUMBERS_OF_DAY = 3
MAX_WITHDRAWALS_VALUE = 500.0

withdrawals = 0

users = []

accounts = []
account_sequence = 0

def create_user(*, CPF, name, date_of_birth, adress ):
    global users

    user_already_exist = [user for user in users if user['CPF'] == CPF]

    if(user_already_exist):
        print('\n Já existe um usuário com esse CPF cadastrado')
    else:
        users.append({
            "CPF": CPF,
            "name": name,
            "date_of_birth": date_of_birth,
            "adress": adress
        })

        print('\n Usuário cadastrado com sucesso!')

def create_account(*, CPF ):
    global users

    global accounts
    global account_sequence

    user_already_exist = [user for user in users if user['CPF'] == CPF]

    if (not user_already_exist):
        print("\n CPF não cadastrado na nossa base de clientes.")
    else:
        account_sequence += 1

        accounts.append({
            "bank_branch": "0001",
            "account_number": account_sequence,
            "CPF": CPF,
            "balance": 0,
            "account_statement": []
        })
        account_sequence + 1

        print('\n Conta cadastrada com sucesso!')


def make_deposit(value, user_account_selected, /):
    global accounts

    if(value <= 0):
        print('\n Valor inválido.')

    else:
        user_account_selected["balance"] += value
        user_account_selected["account_statement"].append(value)

        for account in accounts:
            if(account["account_number"] == user_account_selected["account_number"]):
                user_account_selected
                
        print("\n Operação realizada com sucesso!")

def make_withdrawl(*, value, user_account_selected):
    global accounts
    global withdrawals
    global MAX_WITHDRAWALS_NUMBERS_OF_DAY
    global MAX_WITHDRAWALS_VALUE

    if(value <= 0):
        print('\n Valor inválido.')

    elif((user_account_selected["balance"] - value) < 0):
        print(f'\n Saldo atual de R$ {user_account_selected["balance"]:.2f} insuficiente para realizar a operação.')

    elif(withdrawals >= MAX_WITHDRAWALS_NUMBERS_OF_DAY):
        print('\n Número máximo de 3 saques diários já atingido.')

    elif(value > MAX_WITHDRAWALS_VALUE):
        print(f'\n Saque máximo por operação de R$ {MAX_WITHDRAWALS_VALUE:.2f}')

    else:
        user_account_selected["balance"] -= value
        user_account_selected["account_statement"].append(value * -1)
        withdrawals += 1
        print("\n Operação realizada com sucesso!")

def print_balance(balance, /, *, account_statement):
    if(len(account_statement) == 0):
        print("** Não existem movimentações no período. ** \n")
        print(f"\n Saldo atual de R$ {balance:.2f}  ")

    else:
        print(" *** Extrato do período *** \n")

        for value in account_statement:
            print(f"  R$ {value:.2f}" if (value > 0) else f"- R$ {(value *-1):.2f}")

        print(f"\n Saldo atual de R$ {balance:.2f}  \n")

while True:
    hasAccount = int(input("""
Você já possui uma conta com a gente?

 [1] Sim
 [2] Não
                         
 [9] Sair
                     
"""))
    
    if(hasAccount == 1):
        while True:    
            cpf = input("Digite seu CPF: ")

            user_already_exist = [user for user in users if user['CPF'] == cpf]
            user_accounts = [account for account in accounts if account['CPF'] == cpf]
            user_account_selected = None

            if(not user_already_exist):
                print('\n CPF não cadastrado. Faça seu cadastro antes de começar a usar os nossos serviços.')
                break
            else:

                print(f"Seja bem vindo {user_already_exist[0]["name"]}! \n")
                print("Escolha uma conta para movimentar\n")

                index_accounts = 0
                for account in user_accounts:    
                    index_accounts += 1
                    print(f'[{index_accounts}] Conta {account["account_number"]}') 

                while True:
                    account_number_selected = int(input('\n Selecione o número correspondente a conta que você quer movimentar: \n'))

                    if(account_number_selected > 0 and account_number_selected <= index_accounts):
                        user_account_selected = user_accounts[(account_number_selected - 1)]
                        print(f'Conta selecionada ### {account_number_selected} ### \n')
                        break
                break

        while True:

            type = int(input("""
- - - - - - Escolha a operação - - - - - - 

 [1] Depósito
 [2] Saque
 [3] Extrato
                 
 [9] Retornar ao menu anterior
                     
"""))

            if(type == 1):
                value = float(input('Digite o valor da depósito: '))

                make_deposit(value,user_account_selected)

            elif(type == 2):
                value = float(input('Digite o valor da saque: '))

                make_withdrawl(value=value, user_account_selected=user_account_selected)
                  
            elif(type == 3):
                print_balance(user_account_selected["balance"], account_statement=user_account_selected["account_statement"])
        
            elif(type == 9):
                break

            else:
                print('Operação inválida. Selecione uma das opções do menu \n')

    elif(hasAccount == 2):
        while True:

            type = int(input("""                          
- - - - - - Escolha a operação - - - - - - 

 [1] Criar usuário
 [2] Criar conta
                 
 [9] Retornar ao menu anterior
                     
"""))
        
            if(type == 1):
                print('*** Vamos criar seu usuário *** \n')

                CPF = input('Digite seu CPF (Somente números): ')
                name = input('Digite seu nome: ')
                date_of_birth = input('Digite sua data de nascimento: ')
                adress = input('Digite seu endereço: ')

                create_user(CPF=CPF, name=name, date_of_birth=date_of_birth, adress=adress)

            elif(type == 2):
                print('*** Vamos cadastrar sua conta ***\n')

                CPF = input('Digite seu CPF (Somente números): ')

                create_account(CPF=CPF)

            elif(type == 9):
                break
            
            else:
                print('Operação inválida. Selecione uma das opções do menu \n')

    elif(hasAccount == 9):
        print('Até logo! \n')
        break
    
    else:
        print('Operação inválida. Selecione uma das opções do menu \n')     

    