# this doesn't exactly make sense
# stock wise as you somehow know the future??
import random

prices = []
amt_data_points = random.randint(5, 20)
for _ in range(amt_data_points):
    prices.append(random.randint(0, 9999))
print("There are", amt_data_points, "days available")
print("prices on each of the days:", prices)

day_of_trade = [0, 0]
potential_profit = 0
for buy in range(len(prices)):
    sell = buy + 1
    while sell < len(prices):
        if prices[sell] - prices[buy] > potential_profit:
            potential_profit = prices[sell] - prices[buy]
            day_of_trade = [buy, sell]
        sell += 1
print("the most profit that could of made is", potential_profit,
      "/bought on day:", day_of_trade[0] + 1, "/sold on day:", day_of_trade[1] + 1)
