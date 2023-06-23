# Stock Price Data Filtering using Fast Fourier Transform (FFT)

This Python code utilizes the Fast Fourier Transform (FFT) algorithm to filter stock price data. It uses the `yfinance` library to download historical stock price data from Yahoo Finance and `matplotlib` library for data visualization.
![image](https://github.com/jamiePDunne/pythonMisc/assets/83908748/f15fb686-c6cf-40cc-9381-3e98eb55a2e5)

## Dependencies

Make sure you have the following dependencies installed before running the code:

- `numpy` for numerical operations and FFT.
- `pandas` for data manipulation and analysis.
- `yfinance` for retrieving stock price data.
- `matplotlib` for creating plots.

## Usage

1. Import the necessary libraries at the beginning of your script.
2. Define the start and end dates (`start` and `end`) to specify the time range for the stock price data.
3. Use `yf.download()` to fetch the stock price data for the specified period.
4. Extract the 'Close' prices from the downloaded stock data.
5. Apply the FFT algorithm using `np.fft.fft()` on the 'Close' prices to obtain the frequency domain representation.
6. Calculate the power spectrum by taking the absolute value squared of the FFT results.
7. Determine the cutoff frequency by selecting a percentage (`0.1` in this case) of the maximum frequency.
8. Filter the FFT data by creating a copy of the original FFT results and setting values above the cutoff frequency to zero.
9. Perform an inverse FFT (`np.fft.ifft()`) on the filtered FFT data to obtain the filtered time series.
10. Create a new dataframe (`filtered_data`) to store the filtered prices along with the corresponding dates.
11. Plot the original and filtered time series using `plt.plot()`.
12. Customize the plot by adding labels, titles, and legends.
13. Display the plot using `plt.show()`.

Feel free to modify the code to analyze different stocks or adjust the filtering parameters to suit your needs.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).

Feel free to modify and adapt the code according to your requirements.

Happy filtering and analyzing stock price data!
