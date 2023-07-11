from models.client import Client
from models.account import Account

felicity: Client = Client('Felicity Jones', 'felicity@gmail.com', '123.456.789-01', '02/09/1987')
angelina: Client = Client('Angelina Jones', 'angelina@gmail.com', '321.654.987-01', '02/05/1995')

print(felicity)
print(angelina)

felicityAccount: Account = Account(felicity)

print(felicityAccount)