
# Stock Index Analysis

This Python code enables the analysis of stock index prices using Bollinger Bands and Simple Moving Averages (SMA). It retrieves historical price data for two stock indices from the Yahoo Finance API and plots the price data along with the SMA, upper Bollinger Band (BB), and lower Bollinger Band.

## Dependencies

Make sure you have the following dependencies installed before running the code:

- `yfinance` for retrieving historical price data from Yahoo Finance.
- `plotly.graph_objs` and `plotly.subplots` for creating interactive plots.
- `datetime` and `timedelta` from the `datetime` module for date manipulation.

## Usage

1. Define the stock indices you want to analyze by modifying the `symbols` list. You can add or remove symbols as needed.
2. Set the Bollinger Band and SMA periods by adjusting the `bb_period` and `sma_period` variables, respectively.
3. Specify the start date for the historical data using the `start_date_months` variable. The code retrieves data from the specified number of months ago until the current date.
4. Run the code to download the data for each stock index and calculate the SMA, upper BB, and lower BB.
5. The code will generate an interactive plot with two subplots, each representing a stock index.
6. The subplots display the stock prices, the SMA line, and the upper and lower Bollinger Bands.
7. You can hover over the plot to view specific date and price information for each data point.

## Color Palette

The plot uses the following color scheme:

- Stock Price: darkgray
- SMA Line: darkred
- Upper Bollinger Band: darkblue
- Lower Bollinger Band: darkgreen

Feel free to modify the color values according to your preference.

## Output

The code also includes a section that prints the latest values of the lower BB, upper BB, and SMA for each stock index. This information can be helpful for quick reference.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).

Feel free to modify and adapt the code according to your needs.

Happy analyzing!
