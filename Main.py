import User
import Security
import time


users = []

users.append(User.User(323, "John", "c@gmail.com", "assdds", 240))

list_of_securities = []

list_of_securities.append(Security.Security(929393, 'AAPL', 9566345, 200.0, 1.0e9, time.time()))
list_of_securities[0].update_price(time.time(), 150)

for security in list_of_securities:

    print(security.get_name(), security.calculate_market_cap())
    print(security.get_pricehistory())

users[0].add_stock(list_of_securities[0], 100.0)

users[0].add_stock(list_of_securities[0], 200.0)

print(users[0].get_net_worth())