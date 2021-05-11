# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:23:48 2021
Epoch & Unix Timestamp Conversion Tools
@author: PMR
"""

import pandas as pd
from datetime import datetime

def date_to_unix(time_mark):
    unix = (((pd.to_datetime([time_mark])) - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s'))[0]
    return unix
    
def unix_to_date(unix_mark):
    date = datetime.utcfromtimestamp(unix_mark/1000).strftime('%Y-%m-%d %H:%M:%S')
    return date
