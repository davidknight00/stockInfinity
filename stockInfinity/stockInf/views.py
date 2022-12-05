from django.shortcuts import render
from django.http import HttpResponse
from .forms import TickerForm
import requests
from pygooglenews import GoogleNews

def index(request):
    return render(request, 'index.html')

def account(request):
    return render(request, 'account.html')

def search(request):
    apikey = 'N4T0OWXY9YCO81EI'
    form = TickerForm()
    news = GoogleNews(lang = 'en', country = 'US')
    empty_news = False

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

            # get the news using the company name
            stock_news = news.search(name, when="1m")
            news_info = stock_news['entries']

            # get size of returned news list, if greater than 3 use up to len
            news_size = len(news_info)

            if news_size == 0:
                empty_news = True
            elif news_size < 3:
                # something
                if news_size == 1:
                    title_one = news_info[0].title
                    title_two = ""
                    title_three = ""
                    link_one = news_info[0].link
                    link_two = ""
                    link_three = ""
                else:
                    title_one = news_info[0].title
                    title_two = news_info[1].title
                    title_three = ""
                    link_one = news_info[0].link
                    link_two = news_info[1].link
                    link_three = ""
            else:
                title_one = news_info[0].title
                title_two = news_info[1].title
                title_three = news_info[2].title
                link_one = news_info[0].link
                link_two = news_info[1].link
                link_three = news_info[2].link

            content = {
                    'Ticker': ticker,
                    'Name': name,
                    'Description': desc,
                    'Industry': industry,
                    'MarketCap': market_cap,
                    'YearlyHigh': year_high,
                    'YearlyLow': year_low,
                    'PERatio': pe_ratio,
                    'form': form,
                    'TitleOne': title_one,
                    'TitleTwo': title_two,
                    'TitleThree': title_three,
                    'LinkOne': link_one,
                    'LinkTwo': link_two,
                    'LinkThree': link_three,
                    'empty_news': empty_news
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
        market_cap = f"{int(overview['MarketCapitalization']):,}"
        year_high = f"${float(overview['52WeekHigh']):,}"
        year_low = f"${float(overview['52WeekLow']):,}"
        pe_ratio = f"{overview['PERatio']}x"

        stock_news = news.search(name, when="1m")
        news_info = stock_news['entries']

        # get size of returned news list, if greater than 3 use up to len
        news_size = len(news_info)

        if news_size == 0:
            empty_news = True
        elif news_size < 3:
            if news_size == 1:
                title_one = news_info[0].title
                title_two = ""
                title_three = ""
                link_one = news_info[0].link
                link_two = ""
                link_three = ""
            else:
                title_one = news_info[0].title
                title_two = news_info[1].title
                title_three = ""
                link_one = news_info[0].link
                link_two = news_info[1].link
                link_three = ""
        else:
            title_one = news_info[0].title
            title_two = news_info[1].title
            title_three = news_info[2].title
            link_one = news_info[0].link
            link_two = news_info[1].link
            link_three = news_info[2].link

        content = {
                'Ticker': ticker,
                'Name': name,
                'Description': desc,
                'Industry': industry,
                'MarketCap': market_cap,
                'YearlyHigh': year_high,
                'YearlyLow': year_low,
                'PERatio': pe_ratio,
                'form': form,
                'TitleOne': title_one,
                'TitleTwo': title_two,
                'TitleThree': title_three,
                'LinkOne': link_one,
                'LinkTwo': link_two,
                'LinkThree': link_three,
                'empty_news': empty_news
                }
        return render(request, 'search.html', content)

