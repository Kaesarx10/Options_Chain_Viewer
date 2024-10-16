# Options Chain Viewer with Python, using libraries yfinance, pandas, and matplotlib. 

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Set up user input to determine company 

ticker = input("Company Ticker: ")

# Fetch Options Chain

stock = yf.Ticker(ticker)
options_dates = stock.options

print("Available expiration dates:", options_dates)

# Fetch options data for a specific expiration dates

options_chain = stock.option_chain(options_dates[0])

calls = options_chain.calls

puts = options_chain.puts

print("Calls:\n", calls)
print("Puts:\n", puts)

# Plotting the call Options' strike prices vs their last prices

calls.plot(x='strike', y='lastPrice', kind='line')
plt.show()
