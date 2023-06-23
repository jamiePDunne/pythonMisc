# Momentum Trading Strategy Backtest

This Python code performs a backtest of a momentum trading strategy using historical data from Yahoo Finance. It utilizes the `pandas`, `yfinance`, and `plotly` libraries for data manipulation, downloading stock data, and visualizations, respectively.
![image](https://github.com/jamiePDunne/pythonMisc/assets/83908748/c1242d2d-55ee-4996-afc1-1628be1ec541)

## Dependencies

Make sure you have the following dependencies installed before running the code:

- `pandas` for data manipulation and analysis.
- `yfinance` for retrieving historical stock price data.
- `plotly` for creating interactive plots.

## Usage

1. Import the necessary libraries at the beginning of your script.
2. Use the `yf.download()` function to fetch historical data for the desired stock/index. Adjust the `start` and `end` dates according to your desired time range.
3. Calculate the momentum by subtracting the closing price from the closing price shifted by 50 days.
4. Create a new column called "Momentum Signal" and initialize it to 0.
5. Set the values of the "Momentum Signal" column to 1 when the 50-day momentum is positive.
6. Calculate the daily returns of the closing price using `pct_change()`.
7. Shift the momentum signals by one day to align them with the returns.
8. Calculate the returns for the momentum strategy by multiplying the daily returns by the shifted momentum signal.
9. Calculate the cumulative returns by taking the cumulative product of 1 plus the momentum returns.
10. Plot the cumulative returns using `go.Figure()` and `go.Scatter()`.
11. Customize the plot by adding titles and axis labels.
12. Display the plot using `fig.show()`.

The code also calculates various backtest metrics, including total trades, winning trades, losing trades, win rate, average win, average loss, profit factor, and total return. These metrics are printed in the console.

Feel free to modify the code to test different strategies, adjust the time range, or use different stock/index data.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).

Feel free to modify and adapt the code according to your requirements.

Happy backtesting and exploring momentum trading strategies!
