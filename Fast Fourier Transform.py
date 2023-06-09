import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download stock price data from yfinance
stock_data = yf.download('^gdaxi', start='2023-01-31', end='2023-03-31', interval='1d')

# Extract the 'Close' prices
prices = stock_data['Close']

# Apply FFT
fft = np.fft.fft(prices)
frequencies = np.fft.fftfreq(len(prices))
power_spectrum = np.abs(fft)**2

# Find the cutoff frequency
cutoff_frequency = 0.1 * frequencies.max()

# Filter the FFT data
filtered_fft = fft.copy()
filtered_fft[np.abs(frequencies) > cutoff_frequency] = 0

# Inverse FFT to obtain the filtered time series
filtered_prices = np.fft.ifft(filtered_fft).real

# Create a new dataframe for the filtered prices
filtered_data = pd.DataFrame({'Date': prices.index, 'Filtered_Close': filtered_prices})

# Plot the original and filtered time series
plt.figure(figsize=(10, 6))
plt.plot(prices, label='Original Close Prices')
plt.plot(filtered_data['Date'], filtered_data['Filtered_Close'], label='Filtered Close Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Original and Filtered Close Prices')
plt.legend()
plt.show()
