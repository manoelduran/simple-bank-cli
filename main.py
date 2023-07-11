from typing import List
from time import sleep
from models.client import Client
from models.account import Account


accounts: List[Account] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=====================================')
    print('============== ATM ==================')
    print('=========== Geek Bank ===============')
    print('=====================================')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        createAccount()
    elif opcao == 2:
        withdraw()
    elif opcao == 3:
        deposit()
    elif opcao == 4:
        transfer()
    elif opcao == 5:
        listAccounts()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(2)
        menu()


def createAccount() -> None:
    print('Type some informations to create your bank account:')
    name: str = input('Name: ')
    email: str = input('Email: ')
    cpf: str = input('CPF: ')
    birthDate: str = input('Birth Date: ')
    client: Client = Client(name, email, cpf, birthDate)
    account: Account = Account(client)
    accounts.append(account)
    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print('-----------------')
    print(account)
    sleep(2)
    menu()


def withdraw() -> None:
    if len(accounts) > 0:
        code: int = int(input('Account code:'))
        account: Account = getAccountByCode(code)
        if account:
            value: float = float(input('How much you need?'))
            account.withdraw(value)
        else:
            print('Account with code {code} does not exists!')

    else:
        print('Empty list!')
    sleep(2)
    menu()


def deposit() -> None:
    if len(accounts) > 0:
        code: int = int(input('Account code:'))
        account: Account = getAccountByCode(code)
        if account:
            value: float = float(input('How much you want to save?'))
            account.deposit(value)
        else:
            print('Account with code {code} does not exists!')

    else:
        print('Empty list!')
    sleep(2)
    menu()

def transfer() -> None:
    if len(accounts) > 0:
        code: int = int(input('Account code:'))
        account: Account = getAccountByCode(code)
        if account:
            transferAccountCode: int = int(
                input('Wich account code you want to transfer?:'))
            transferAccount: Account = getAccountByCode(transferAccountCode)
            if transferAccount:
                value: float = float(input('How much you want to transfer?'))
                account.transfer(transferAccount, value)
            else:
                print('Account with code {code} does not exists!')
        else:
            print('Account with code {code} does not exists!')

    else:
        print('Empty list!')
    sleep(2)
    menu()

def listAccounts() -> None:
    if len(accounts) > 0:
        for account in accounts:
            print(account)
            print('--------------------')
            sleep(1)
    else:
        print('Empty list!')
    sleep(2)
    menu()


def getAccountByCode(code: int) -> Account:
    foundAccount: Account = None
    if len(accounts) > 0:
        for account in accounts:
            if account.code == code:
                foundAccount = account
        return foundAccount
    else:
        print('No accounts registered in our system!')


if __name__ == '__main__':
    main()
