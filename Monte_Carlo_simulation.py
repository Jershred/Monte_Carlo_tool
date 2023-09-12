# -*- coding: utf-8 -*-
"""
Created on Thu Sep 5 18:31:35 2023

This code generates a Monte Carlo Simulation using historical price data. 
It calculates historical log returns and forecasts the probability 
distribution of final stock prices after X days. Additionally, it visualizes 
each day's simulated path of prices on a graph.

@author: Jérémy Archier
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from scipy.stats import norm

# Function to load historical stock data from a CSV file
def load_stock_data(csv_file_path):
    dates = []
    opens = []

    with open(csv_file_path, newline="") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            if row['Open'].strip() == '' or row['Open'].lower() == 'null' or float(row['Open']) == 0:
                continue

            open_value = float(row['Open'])
            date_value = datetime.strptime(row['Date'], '%Y-%m-%d')

            dates.append(date_value)
            opens.append(open_value)

    return dates, opens

# Function to plot historical stock prices
def plot_historical_stock_prices(stock_data):
    for i, stock_file in enumerate(stock_data):
        stock_symbol = stock_file.split(".")[0]
        dates, opens = load_stock_data(stock_file)

        plt.figure(figsize=(10, 6))
        plt.plot(dates, opens, label=stock_symbol)
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        plt.title(f'Historical Stock Prices for {stock_symbol}')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# Function to calculate log returns from open prices
def calculate_log_returns(opens):
    log_returns = np.log(np.array(opens[1:]) / np.array(opens[:-1]))
    return log_returns

# Function to perform Monte Carlo simulation for a single stock
def monte_carlo_simulation_single_stock(trials, days, log_returns, current_price, initial_investment, stock_symbol, plot_simulation=True):
    # Calculate drift and volatility
    u = log_returns.mean()
    var = log_returns.var()
    drift = u - (0.5 * var)
    stdev = log_returns.std()

    # Generate random returns
    Z = norm.ppf(np.random.rand(days, trials))
    daily_returns = np.exp(drift + stdev * Z)

    # Simulate price paths
    price_paths = np.zeros((days, trials))
    price_paths[0] = current_price

    for t in range(1, days):
        price_paths[t] = price_paths[t - 1] * daily_returns[t]

    final_prices = price_paths[-1, :]
    portfolio_values = final_prices * (initial_investment / current_price)

    if plot_simulation:
        # Plot Monte Carlo Simulation of stock price
        plot_stock_price_paths(price_paths, stock_symbol)

    # Calculate individual stock returns for each trial
    individual_stock_returns = ((final_prices - current_price) / current_price) * 100

    return portfolio_values, individual_stock_returns

# Function to plot price paths for a single stock
def plot_stock_price_paths(price_paths, stock_symbol):
    plt.figure(figsize=(10, 6))
    for trial in range(trials):
        plt.plot(price_paths[:, trial], linewidth=0.5)
    plt.xlabel('Days')
    plt.ylabel('Stock Price')
    plt.title(f'Monte Carlo Simulation of {stock_symbol} Stock Price')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# Function to plot the histogram of final stock prices
def plot_final_stock_price_histogram(final_prices, current_price, stock_symbol):
    plt.figure(figsize=(10, 6))
    plt.hist(final_prices, bins=30, edgecolor='k', density=True)
    plt.axvline(x=current_price, color='r', linestyle='dashed', linewidth=2, label=f'Initial investment in {stock_symbol} (${current_price:.2f})')
    plt.xlabel('Stock Price')
    plt.ylabel('Probability Density')
    plt.title(f'Probability Distribution of Final {stock_symbol} Stock Prices')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Function to perform Monte Carlo simulation for a portfolio of stocks
def monte_carlo_simulation_portfolio(stock_files, weights, trials, days, initial_investment, plot_stock_simulation=True):
    portfolio_returns = []
    portfolio_values = np.zeros((days, trials))
    stock_symbols = []
    
    # Plot historical stock prices
    plot_historical_stock_prices(stock_files)

    for i, stock_file in enumerate(stock_files):
        stock_symbol = stock_file.split(".")[0]
        dates, opens = load_stock_data(stock_file)
        log_returns = calculate_log_returns(opens)
        current_price = opens[-1]

        stock_portfolio_values, individual_stock_returns = monte_carlo_simulation_single_stock(trials, days, log_returns, current_price, initial_investment * weights[i], stock_symbol, plot_simulation=plot_stock_simulation)
        portfolio_values += stock_portfolio_values

        average_stock_return = np.mean(individual_stock_returns)  # Calculate the average return for the stock

        portfolio_returns.append(average_stock_return)
        stock_symbols.append(stock_symbol)

        # Plot final stock price histogram
        plot_final_stock_price_histogram(stock_portfolio_values, initial_investment * weights[i], stock_symbol)
        

    # Plot the histogram of final portfolio values
    final_portfolio_values = portfolio_values[-1, :]
    plt.figure(figsize=(10, 6))
    plt.hist(final_portfolio_values, bins=30, edgecolor='k', density=True)
    plt.axvline(x=initial_investment, color='r', linestyle='dashed', linewidth=2, label=f'Initial investment (${initial_investment:.2f})')
    plt.xlabel('Portfolio Value')
    plt.ylabel('Probability Density')
    plt.title('Probability Distribution of Final Portfolio Values')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot the pie chart for portfolio composition
    plot_portfolio_pie_chart(weights, stock_symbols)

    # Display stock returns as a bar chart
    display_stock_returns(stock_symbols, portfolio_returns)

# Function to plot a pie chart showing the composition of the portfolio
def plot_portfolio_pie_chart(weights, stock_symbols):
    plt.figure(figsize=(8, 8))
    plt.pie(weights, labels=stock_symbols, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    
    # Increase the title spacing and set a larger title font size
    plt.title('Portfolio Composition', pad=30, fontsize=16)  # Adjust pad and fontsize as needed
    
    # Customize the legend (labels) with larger font size
    plt.legend(stock_symbols, title='Stock Symbols', fontsize=12, loc='upper left')  # Adjust fontsize as needed
    
    plt.show()

# Function to display stock returns as a bar chart
def display_stock_returns(stock_symbols, stock_returns):
    plt.figure(figsize=(10, 6))
    plt.bar(stock_symbols, stock_returns)
    plt.xlabel('Stocks')
    plt.ylabel('Average Returns (%)')
    plt.title('Average Returns of Individual Stocks in the Portfolio')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


###############################################################################
##################################### Main ####################################
###############################################################################


# Define the list of stock data files and their corresponding weights in the portfolio
stock_data = ["SAF.PA.csv", "AIR.PA.csv", "UBS.csv"]  # Replace with your stock data files
weights = [0.4, 0.3, 0.3]  # Replace with the weights of each stock in the portfolio; the sum must be equals 1
initial_investment = 1000  # Initial investment amount
trials = 100 # Minimum of 1,000 to 5,000 trials is considered a reasonable starting point for basic simulations
days = 365

# Enable stock price path visualization with consideration for potential performance slowdown, especially for a large number of trials.
plot_stock_simulation=True

monte_carlo_simulation_portfolio(stock_data, weights, trials, days, initial_investment, plot_stock_simulation)