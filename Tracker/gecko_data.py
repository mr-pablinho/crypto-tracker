# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:39:52 2021
Check value of coins in a period of time
@author: PMR
"""

from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import time
import time_conversor as tc

# set CoinGecko API onject
cg = CoinGeckoAPI()

# conditons for evaluation
coin_list = cg.get_coins_list()
base_currency = 'usd'
crypto = ['ethereum', 'monero', 'bitcoin-cash']

# from_unix = time.mktime(datetime(2021, 5, 7, 12, 00).timetuple())
from_ts = tc.date_to_unix('2020-01-01 00:00:00')
to_ts   = tc.date_to_unix('2021-05-06 00:00:00')


for i in range(len(crypto)):
    
    # get chart from CoinGecko API    
    chart = cg.get_coin_market_chart_range_by_id(crypto[i], base_currency, from_ts, to_ts)
    coin_data = cg.get_coin_by_id(crypto[i])
    coin_name, coin_symbol = coin_data['name'], coin_data['symbol']

    # create list with prices and dates
    date   = [(chart['prices'][ii][0]) for ii in range(len(chart['prices']))]
    prices = [(chart['prices'][ii][1]) for ii in range(len(chart['prices']))]        
    date_str = [tc.unix_to_date(date[ii]) for ii in range(len(date))]
    dates_list = pd.to_datetime(date_str, format='%Y-%m-%d %H:%M:%S.%f')
    
    # plot results
    plt.figure('Price-time')
    plt.plot(dates_list, prices, linewidth=1, label=coin_name)
    plt.ylabel('Price [' + base_currency + ']')
    plt.xlabel('Date')
    plt.xticks(rotation=25)
    plt.legend()
    


