# Index Price Analysis

This Python code performs an analysis of index prices using historical data obtained from Yahoo Finance. It utilizes the `matplotlib` and `yfinance` libraries for data visualization and retrieving stock price data, respectively.

## Dependencies

Make sure you have the following dependencies installed before running the code:

- `matplotlib` for data visualization.
- `yfinance` for retrieving historical stock price data.

## Usage

1. Import the necessary libraries at the beginning of your script.
2. Use the `yf.download()` function to fetch historical data for the desired index or stock. Adjust the `start` and `end` dates according to your desired time range.
3. Plot the raw closing prices by calling `index['Close'].plot()` and customizing the plot as needed.
4. Display the plot using `plt.show()`.

The code also calculates and visualizes the min-max transformation of the index prices. It calculates the rolling maximum and minimum prices using a specified window size (`rollingDays`). It then normalizes the closing prices within the range of 0 to 1 by applying the min-max transformation. The normalized prices are plotted using `index['norm'].plot()` and displayed using `plt.show()`.

Feel free to modify the code to analyze different indices, adjust the time range, or customize the plot styles according to your preferences.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).

Feel free to modify and adapt the code according to your requirements.

Happy analyzing index prices!
