# Monte Carlo Simulation Code Readme

**Author**: Jérémy Archier
**Date**: September 5, 2023

## Overview

This code provides a Monte Carlo Simulation using historical price data for a portfolio of stocks. It calculates historical log returns and forecasts the probability distribution of final stock prices after a specified number of days. Additionally, it visualizes each day's simulated path of prices on a graph. The code is designed to be flexible, allowing you to input your own stock data files and weights for the portfolio.

## Getting Started

1. **Requirements**: Ensure you have the necessary libraries installed, including `numpy`, `matplotlib`, `datetime`, and `scipy`. You can install these libraries using pip:

   ```
   pip install numpy matplotlib scipy
   ```

2. **Data Preparation**: Prepare your historical stock price data in CSV format. The CSV file should have columns for "Date" and "Open" prices. Make sure the CSV file is in the same directory as this script.

3. **Define Portfolio**: In the main section of the code, define the list of stock data files (`stock_data`), their corresponding weights (`weights`) in the portfolio, the initial investment amount (`initial_investment`), the number of trials (`trials`), and the number of days for the simulation (`days`).

## Code Structure

- **load_stock_data**: A function to load historical stock data from a CSV file.
- **plot_historical_stock_prices**: Function to plot historical stock prices for all stocks in the portfolio.
- **calculate_log_returns**: Function to calculate log returns from open prices.
- **monte_carlo_simulation_single_stock**: Perform Monte Carlo simulation for a single stock with gradient coloring. It calculates drift, volatility, and simulates price paths.
- **plot_stock_price_paths**: Function to plot price paths for a single stock with gradient coloring.
- **plot_final_stock_price_histogram**: Function to plot the histogram of final stock prices.
- **monte_carlo_simulation_portfolio**: Perform Monte Carlo simulation for a portfolio of stocks. It iterates over stocks, calculates portfolio values, and visualizes results.
- **plot_portfolio_pie_chart**: Function to plot a pie chart showing the composition of the portfolio.
- **display_stock_returns**: Function to display stock returns as a bar chart.

## Usage

After configuring the parameters in the main section, run the script. It will perform the Monte Carlo simulation and display various visualizations:

1. Historical stock price plots for all stocks in the portfolio.
2. Monte Carlo simulation of stock price paths with gradient coloring.
3. Probability distribution of final stock prices for each stock in the portfolio.
4. Probability distribution of final portfolio values.
5. Pie chart showing the composition of the portfolio.
6. Bar chart displaying the average returns of individual stocks in the portfolio.

## Note

- The code uses Monte Carlo simulation for forecasting, and the accuracy of results depends on the number of trials (`trials`). A minimum of 1,000 to 5,000 trials is considered reasonable for basic simulations.
- This code is for educational and illustrative purposes. Ensure that you have proper data and risk management practices in place for real financial decisions.

Feel free to customize the code to suit your specific needs and add error handling or additional features as necessary.

## References

This code is based on Monte Carlo simulation techniques and utilizes libraries such as NumPy, Matplotlib, and SciPy. For more details on these libraries and the Monte Carlo method, refer to their respective documentation:

- NumPy: [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
- Matplotlib: [https://matplotlib.org/stable/users/index.html](https://matplotlib.org/stable/users/index.html)
- SciPy: [https://docs.scipy.org/doc/scipy/reference/](https://docs.scipy.org/doc/scipy/reference/)

## License

This code is provided under the MIT License. You are free to use, modify, and distribute it as needed.
