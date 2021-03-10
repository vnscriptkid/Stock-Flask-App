import requests

API_URL_BASE = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'
API_KEY = '2bdb777263f766d57eb0dd3831cefabf'


def get_price(ticker):
    url = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'.format(ticker)
    data = requests.get(url, params={'apikey': API_KEY}).json()
    return data["price"]


def get_financials(ticker):
    url = 'https://financialmodelingprep.com/api/v3/financials/income-statement/{}'.format(ticker)
    data = requests.get(url, params={'period': 'quarter', 'apikey': API_KEY}).json()
    return data['financials']


def eps_chart_url(financials):
    chart_data = [float(q["EPS"]) for q in financials]

    chart_params = {"type": 'line',
                    "data": {
                        'labels': [q["date"] for q in financials],
                        'datasets': [{'label': 'EPS', 'data': chart_data}]
                    }}

    return "https://quickchart.io/chart?width=500&height=200&c={}".format(chart_params)

