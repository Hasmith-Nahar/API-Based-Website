import requests
from flask import Flask, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "some secret key"

BASE_URL = "http://api.marketstack.com/v1/tickers?access_key="
API_KEY = "9797fcf81940209f01b0f443107e2ace"

endpoint = BASE_URL + API_KEY


def get_stocks():
    response = requests.get(endpoint).json()
    return response['data']


@app.route('/all-stocks')
def get_all_stocks():
    return jsonify(get_stocks())


if __name__ == '__main__':
    app.run(debug=True)
