from models.client import Client
from utils.helper import formatFloatCoinToStr


class Account:
    counter: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__code: int = Account.code
        self.__client: Client = client
        self.__currentBalance: float = 0.0
        self.__limit: float = 100.0
        self.__totalBalance: float = self.calculateTotalBalance
        Account.counter += 1

    def __str__(self) -> str:
        return f'Account Number: {self.code} \nClient: {self.client.name} \n Total Balance: {formatFloatCoinToStr(self.totalBalance)} '

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def client(self: object) -> Client:
        return self.__client

    @property
    def currentBalance(self: object) -> float:
        return self.__currentBalance

    @currentBalance.setter
    def currentBalance(self: object, value: float) -> None:
        self.__currentBalance = value

    @property
    def limit(self: object) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def totalBalance(self: object) -> float:
        return self.__totalBalance

    @totalBalance.setter
    def totalBalance(self: object, value: float) -> None:
        self.__totalBalance = value

    @property
    def calculateTotalBalance(self: object) -> float:
        return self.currentBalance + self.limit

    def deposit(self: object, value: float) -> None:
        if value > 0:
            self.currentBalance = self.currentBalance + valor
            self.totalBalance = self.calculateTotalBalance
            print('Deposit successfully!')
        else:
            print('Deposit unsuccessfully! Try again!')
    def withdraw(self: object, value: float) -> None:
        if 0 < value <= self.totalBalance:
            if self.currentBalance >= value:
                self.currentBalance = self.totalBalance - value
            else:
                rest: float = self.totalBalance - value
                self.limit = self.limit + rest
                self.currentBalance = 0
                self.totalBalance = self.calculateTotalBalance
            print('Withdraw successfully!')
        else:
            print('Withdraw unsuccessfully! Try again!')

    def transfer(self: object, destiny: object, value: float) -> None:
        if value > 0 and self.totalBalance >= value:
            if self.currentBalance >= value:
                self.currentBalance = self.currentBalance - value
                self.totalBalance = self._calcula_totalBalance
                destiny.currentBalance = destiny.currentBalance + value
                destiny.totalBalance = destiny._calcula_totalBalance
            else:
                restante: float = self.currentBalance - value
                self.currentBalance = 0
                self.limite = self.limite + restante
                self.totalBalance = self._calcula_totalBalance
                destiny.currentBalance = destiny.currentBalance + value
                destiny.totalBalance = destiny.calculateTotalBalance
            print('Transfer successfully!')
        else:
            print('Transfer unsuccessfully! Try again!')
