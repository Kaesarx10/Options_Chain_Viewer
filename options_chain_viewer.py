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
