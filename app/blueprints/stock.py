from flask import Blueprint, render_template

from app.stock_data import get_price, get_financials, eps_chart_url

stock = Blueprint('stock', __name__, url_prefix='/stocks')


@stock.route('/<string:ticker>')
def view_stock(ticker):
    stock_price = get_price(ticker)
    return render_template('stock/stock_quote.html', ticker=ticker, stock_price=stock_price)


@stock.route('/<string:ticker>/financials')
def financials(ticker):
    financials = get_financials(ticker)
    return render_template('stock/financials.html', ticker=ticker, financials=financials, chart_url=eps_chart_url(financials))


