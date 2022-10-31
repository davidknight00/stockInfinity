from django.shortcuts import render
from django.http import HttpResponse
from .forms import TickerForm
import requests

def index(request):
    return render(request, 'index.html')

def account(request):
    return render(request, 'account.html')

def search(request):
    apikey = 'N4T0OWXY9YCO81EI'
    form = TickerForm()

    if request.method == 'POST':
        ticker = request.POST.get('ticker').upper()
        url = 'https://www.alphavantage.co/query'
        param1 = {'function': 'OVERVIEW', 'symbol': ticker, 'apikey': apikey}
        param2 = {'function': 'TIME_SERIES_INTRADAY', 'symbol': ticker, 'interval': '5min', 'apikey': apikey}

        # use urls and params to get stock information on requested ticker
        overview = requests.get(url, params=param1)
        overview = overview.json()

        stock_tsi = requests.get(url, params=param2)
        stock_tsi = stock_tsi.json()

        try:
            name = overview['Name']
            desc = overview['Description']
            industry = overview['Industry']
            market_cap = overview['MarketCapitalization']
            year_high = overview['52WeekHigh']
            year_low = overview['52WeekLow']
            pe_ratio = overview['PERatio']

            content = {
                    'Ticker': ticker,
                    'Name': name,
                    'Description': desc,
                    'Industry': industry,
                    'MarketCap': market_cap,
                    'YearlyHigh': year_high,
                    'YearlyLow': year_low,
                    'PERatio': pe_ratio,
                    'form': form
                    }

            return render(request, 'search.html', content)

        except:
            return render(request, '404.html', {'response_code': 'Data could not be retrieved, does this stock exist?'})
    else:
        # first page load - use AAPL for now until search occurs
        #TODO: make first ticker random for stock of the day
        ticker = 'AAPL'
        url = 'https://www.alphavantage.co/query'
        param1 = {'function': 'OVERVIEW', 'symbol': ticker, 'apikey': apikey}
        param2 = {'function': 'TIME_SERIES_INTRADAY', 'symbol': ticker, 'interval': '5min', 'apikey': apikey}

        # use urls and params to get stock information on requested ticker
        overview = requests.get(url, params=param1)
        overview = overview.json()

        stock_tsi = requests.get(url, params=param2)
        stock_tsi = stock_tsi.json()

        name = overview['Name']
        desc = overview['Description']
        industry = overview['Industry']
        market_cap = overview['MarketCapitalization']
        year_high = overview['52WeekHigh']
        year_low = overview['52WeekLow']
        pe_ratio = overview['PERatio']

        content = {
                'Ticker': ticker,
                'Name': name,
                'Description': desc,
                'Industry': industry,
                'MarketCap': market_cap,
                'YearlyHigh': year_high,
                'YearlyLow': year_low,
                'PERatio': pe_ratio,
                'form': form
                }
        return render(request, 'search.html', content)

