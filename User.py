# Created on Apr 23, 2017
# @author: cmlpr

import sys
import time


class User(object):
    '''
    User class
    '''

    userObjCount = 0

    @staticmethod
    def status():
        print("Total number of users is = ", User.userObjCount)

    def __init__(self, idno, username, email, password, dollars=50, portfolio=dict()):

        User.userObjCount += 1

        self.__id = idno
        self.__username = username
        self.__email = email
        self.__password = password
        self.__dollars = dollars
        self.__portfolio = portfolio
        self.__record = []

    def update_email(self, new_email):

        self.__email = new_email

    def change_password(self, new_password):

        self.__password = new_password

    def update_currency(self, dollars):

        self.__dollars += dollars

    def add_stock(self, stock, quantity):

        if stock in self.__portfolio:
            self.__portfolio[stock] += quantity
        else:
            self.__portfolio[stock] = quantity

        self.__record.append((stock, quantity, time.time()))

    def remove_stock(self, stock, quantity):

        if stock in self.__portfolio:
            if self.__portfolio[stock] >= quantity:
                self.__portfolio[stock] -= quantity
            else:
                sys.exit("Tried to remove more shares than the user currently holds!")
        else:
            sys.exit("Tried to remove a stock which doesn't exist in user's portfolio")

        self.__record.append((stock, quantity, time.time()))

    def get_net_worth(self):

        worth = 0.0
        for stock, quantity in self.__portfolio.items():
            worth += stock.get_price() * quantity

        return worth
