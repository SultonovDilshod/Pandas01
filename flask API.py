from flask import Flask, jsonify

from bs4 import BeautifulSoup as bs
import requests


def get_currency(int_cur, out_cur):
    url = f'https://www.x-rates.com/calculator/?from={int_cur}&to={out_cur}&amount=1'
    respod = requests.get(url).text
    soup = bs(respod, 'html.parser')
    currency = soup.find("span", class_=('ccOutputRslt')).get_text()
    rate = currency.split(' ')[0]
    return rate


app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Currency Rate API</h1><p>Example URL: /api/v1/usd-eur</p>'


@app.route('/api/v1/<int_cur>-<out_cur>')
def currency(int_cur, out_cur):
    rate = get_currency(int_cur, out_cur)
    result = {'input_currency': int_cur, 'output_currency': out_cur, 'rate':rate}
    return jsonify(result)


app.run(host='0.0.0.0')
