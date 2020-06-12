import requests
import numpy as np
import pandas as pd
import datetime
from datetime import timedelta
import json
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px


def get_data(currencies, base = 'SGD'):
    year = timedelta(days = 365)
    today = datetime.date.today()
    start = (today-year).isoformat()
    end = today.isoformat()
    curs = currencies #required currencies, separated by commas
    base = base
    url = 'https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols={}&base={}'.format(start,end,curs,base)
    r = requests.get(url)
    rates = r.json()['rates']
    #gotten response from API

    df = pd.DataFrame(rates)
    df = df.transpose()
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace = True)

    windows = [20,60]
    
    #generate SMA
    for window in windows:
        df['SMA{}'.format(window)] = df.iloc[:,0].rolling(window,min_periods = 0).mean()
        df['SMA{}-1'.format(window)] = df['SMA{}'.format(window)].shift(-1)
        df['SMA{}_diff'.format(window)] = df['SMA{}'.format(window)] - df['SMA{}-1'.format(window)]
        df['SMA{}dir'.format(window)] = df['SMA{}_diff'.format(window)].apply(lambda x: True if x < 0 else False)
        df['SMA{}std_dev'.format(window)] = df.iloc[:,0].rolling(window,min_periods = 0).std()
    
    #processing spot data
    spot_info = df.iloc[-1,:]
    spot_price = spot_info[0]
    spot_SMA = dict()
    spot_SD = dict()

    for window in windows:
        spot_SMA[window] = spot_info['SMA{}'.format(window)]
        spot_SD[window] = spot_info['SMA{}std_dev'.format(window)]
    
    signal = 'The spot price is {:.4f}'.format(spot_price)
    spot = list()
    spot.append(signal)

    for window in spot_SMA:
        
        pos = None
        
        if spot_price < spot_SMA[window]:
            pos = 'lower'
        else: pos = 'higher'

        trading_SD = (spot_price-spot_SMA[window])/spot_SD[window]
        msg = 'It is now trading at {:.4f} of standard deviation of {} days moving average'.format(trading_SD, window)
        spot.append(msg)


    return spot

def get_chart(currencies, base = 'SGD'):
    year = timedelta(days = 365)
    today = datetime.date.today()
    start = (today-year).isoformat()
    end = today.isoformat()
    curs = currencies #required currencies, separated by commas
    base = base
    url = 'https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols={}&base={}'.format(start,end,curs,base)
    r = requests.get(url)
    rates = r.json()['rates']
    #gotten response from API
    df = pd.DataFrame(rates)
    df = df.transpose()
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace = True)
    df['SMA30'] = df.iloc[:,0].rolling(30,min_periods = 0).mean()

    fig = go.Figure()
    scatter = go.Scatter(x = df.index , y = df.iloc[:,0], name = curs)
    scatter30 = go.Scatter(x = df.index , y = df.loc[:,'SMA30'], name = 'SMA30')
    fig.add_trace(scatter)
    fig.add_trace(scatter30)
    
    plt_div = plot(fig, output_type = 'div', include_plotlyjs= False)
    spot_price = df.iloc[-1,0]
    sma_price = df.iloc[-1,1]
    fx_data = {
        'plt_div':plt_div,
        'spot_price':spot_price,
        'sma_price': sma_price
    }

    return fx_data


#print(get_data('HKD')) #returns spot price successfully; API call successful.

class Currency_Pair_data():
    data = None
    