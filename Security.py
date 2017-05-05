# Created on Apr 25, 2017
# @author: cmlpr

import sys


class Security(object):
    '''
    Security class
    '''

    securityObjCount = 0

    @staticmethod
    def status():
        print("Total number of securities = ", Security.securityObjCount)

    def __init__(self, idn, security_name, total_shares, price, cash_balance, time_stamp):

        Security.securityObjCount += 1

        self.__id = idn
        self.__name = security_name
        self.__shares_outstanding = total_shares
        self.__current_price = price
        self.__cash_balance = cash_balance
        self.__price_history = [(time_stamp, price)]
        self.__dividend_history = []
        self.__top_bid = None
        self.__top_ask = None
        self.__open_bids = []
        self.__open_asks = []

    def update_price(self, time_stamp, new_price):

        self.__current_price = new_price
        self.__price_history.append((time_stamp, new_price))

    def calculate_market_cap(self):
        return self.__current_price * float(self.__shares_outstanding)

    def add_bid(self, time_stamp, bid_price, bid_amount):
        self.__top_bid = (time_stamp, bid_price, bid_amount)
        self.__open_bids.append((time_stamp, bid_price, bid_amount))

    def add_ask(self, time_stamp, ask_price, ask_amount):
        self.__top_ask = (time_stamp, ask_price, ask_amount)
        self.__open_asks.append((time_stamp, ask_price, ask_amount))

    def update_cash_balance(self, amount):
        self.__cash_balance += amount

    def yield_dividend(self, time_stamp, dividend_amount):
        self.__dividend_history.append((time_stamp, dividend_amount))

    def get_name(self):
        return self.__name

    def get_pricehistory(self):
        return self.__price_history

    def get_price(self):
        return self.__current_price
