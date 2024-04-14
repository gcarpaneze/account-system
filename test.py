users = []

accounts = []
account_sequence = 0

def create_user(*, CPF, name, date_of_birth, adress ):
    global users

    user_already_exist = [user for user in users if user['CPF'] == CPF]

    if(user_already_exist):
        print('Já existe um usuário com esse CPF cadastrado')
    else:
        users.append({
            "CPF": CPF,
              "name": name,
                "date_of_birth": date_of_birth,
                  "adress": adress
        })

def create_account(*, CPF ):
    global users

    global accounts
    global account_sequence

    user_already_exist = [user for user in users if user['CPF'] == CPF]

    if (not user_already_exist):
        print('CPF não cadastrado na nossa base de clientes.')
    else:
        account_sequence += 1

        accounts.append({
            "bank_branch": "0001",
            "account_number": account_sequence,
            "CPF": CPF
        })
        account_sequence + 1