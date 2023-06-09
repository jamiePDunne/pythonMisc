# BTC-USD Simple Moving Average (SMA) Analysis

This Python code analyzes the BTC-USD price data using Simple Moving Averages (SMA) and identifies the "Death Cross" pattern. It utilizes the `yfinance` library to fetch historical price data from Yahoo Finance and `matplotlib` library for plotting.

## Dependencies

Before running the code, ensure that you have the following dependencies installed:

- `yfinance` for retrieving historical price data from Yahoo Finance.
- `matplotlib` for creating plots.

## Usage

1. Import the necessary libraries at the beginning of your script.
2. Specify the `start` and `end` dates to determine the time range for the price data.
3. Use `yf.download()` to fetch the BTC-USD price data from Yahoo Finance within the specified time range.
4. Calculate the 50-day and 200-day Simple Moving Averages (SMA) using the `rolling().mean()` function on the "Close" price data.
5. Ensure that both SMAs start from the same point by dropping any rows with missing values (NaN) using `dropna()`.
6. Determine the occurrence of the "Death Cross" pattern by comparing the 50-day SMA with the 200-day SMA. A value of 1 is assigned to the "death_x" column if the 50-day SMA is less than the 200-day SMA; otherwise, it is assigned 0.
7. Store the timestamps of the triggered "Death Cross" events in the `list_death_x_ts` list.
8. Plot the BTC-USD price, 50-day SMA, 200-day SMA, and mark the "Death Cross" events using `plt.subplots()` and `axvline()` functions.
9. Customize the plot appearance and layout as desired.
10. Display the plot using `plt.show()`.

Feel free to modify the code to analyze different cryptocurrencies or adjust the SMA periods to suit your requirements.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).

Feel free to modify and adapt the code according to your needs.

Happy analyzing and trading!
