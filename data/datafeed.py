#!/usr/bin/env python
""" datafeed.py
Data sources
"""
from ..database import Client

class IntradayQuotes(object):
    """
    API for retreiving intraday quotes from the stock database
    """
    def __init__(self):
        self.stock_db = Client()


    def get_quote(self, ticker, date):
        """
        Return a quote for the given stock on the given date
        """
        return self.stock_db.get_quotes(ticker, date)[0]


    def get_quotes(self, ticker, start_date, end_date):
        """
        Return a list of quotes for the given stoc from start_date to end-date
        """
        return self.stock_db.get_quotes(ticker, start_date, end_date)


class TickQuotes(object):
    """
    API for retreiving tick-by-tick data from the stock database
    """
    def __init__(self):
        self.stock_db = Client()
    
    def get_quotes(self, ticker):
        pass
    