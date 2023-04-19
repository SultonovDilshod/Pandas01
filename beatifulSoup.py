from bs4 import BeautifulSoup as bs
import requests

a = input("Enter first currency short like USD:")
b = input("Enter second currency short like EUR:")

def get_currency(input_currency, output_currency):
    url = f'https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1'
    respod = requests.get(url).text
    soup = bs(respod, 'html.parser')
    currency = soup.find("span", class_=('ccOutputRslt')).get_text()
    print(currency.split(' ')[0])


get_currency(a, b)






