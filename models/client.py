from datetime import date
from utils.helper import dateToStr, strToDate


class Client:
    counter: int = 101

    def __init__(self: object, name: str, email: str, cpf: str, birthDate: str) -> None:
        self.__code: int = Client.counter
        self.__name: str = name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__birthDate: date = strToDate(birthDate)
        self.__created_at: date = date.today()
        Client.counter += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def birthDate(self: object) -> date:
        return self.__birthDate

    @property
    def created_at(self: object) -> str:
        return dateToStr(self.__created_at)

    def __str__(self) -> str:
        return f'Code: {self.code} \nName: {self.name} \nBirth Date: {self.birthDate} \nCreated At: {self.created_at}'
