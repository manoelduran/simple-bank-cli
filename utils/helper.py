from datetime import date
from datetime import datetime

def dateToStr(data: date) -> str:
    return data.strftime('%d/%m/%Y')

def strToDate(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')

def formatFloatCoinToStr(value: float) -> str:
    return f'R$ {value:,.2f}'