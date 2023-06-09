
# BTC-USD Performance and Z-Score Analysis

This Python code demonstrates the calculation of the Z-Score for BTC-USD performance using historical price data obtained from the Yahoo Finance API. The Z-Score is a statistical measure that indicates how many standard deviations an observation or data point deviates from the mean of a distribution.

## Dependencies

This code relies on the following libraries:

- `yfinance` for retrieving historical price data from Yahoo Finance.
- `pandas` for data manipulation and analysis.
- `plotly.graph_objs` and `plotly.subplots` for creating interactive plots.

Please make sure you have these libraries installed before running the code.

## Usage

1. Set the `rollingWindow` variable to define the rolling window size for the calculation of the Z-Score. It represents the number of days used to calculate the mean and standard deviation.
2. Set the `zlag` variable to specify the lag for the Z-Score calculation.
3. Run the code to retrieve BTC-USD historical price data and calculate the Z-Score.
4. An interactive plot will be displayed showing the BTC-USD closing prices, the calculated Z-Score, and the lagged Z-Score.
5. You can hover over the plot to see the date and corresponding values for each data point.

Note: This code retrieves two years of historical price data from the Yahoo Finance API by default. You can adjust the `start_date` and `end_date` variables to fetch data for a different time range if needed.

## Plot Configuration

The plot includes the following components and features:

- The BTC-USD closing prices are displayed on the primary y-axis.
- The Z-Score values are shown on the secondary y-axis.
- The Z-Score Lagged values are also displayed on the secondary y-axis.
- A zero line is included on the Z-Score y-axis for reference.
- Crosshair and hovermode are enabled for easy exploration of the data.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).

Feel free to modify and adapt the code according to your needs.

Happy coding!
