import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

# Define the symbols for the 2 stock indices
symbols = ['^GSPC', '^GDAXI']

# Define the Bollinger Band and SMA periods
bb_period = 20
sma_period = 50

# Define the start date for the data based on the number of months
start_date_months = 36
start_date = (datetime.today() - timedelta(days=start_date_months*30)).strftime('%Y-%m-%d')

# Download the data for each symbol
data = {}
for symbol in symbols:
    data[symbol] = yf.download(symbol, start=start_date)

# Calculate the Bollinger Bands and SMA for each symbol
for symbol in symbols:
    data[symbol]['sma'] = data[symbol]['Close'].rolling(window=sma_period).mean()
    data[symbol]['std'] = data[symbol]['Close'].rolling(window=bb_period).std()
    data[symbol]['upper_bb'] = data[symbol]['sma'] + 2 * data[symbol]['std']
    data[symbol]['lower_bb'] = data[symbol]['sma'] - 2 * data[symbol]['std']

# Define the color palette
price_color = 'darkgray'
sma_color = 'darkred'
upper_bb_color = 'darkblue'
lower_bb_color = 'darkgreen'

# Create a 2x1 subplot grid
fig = make_subplots(rows=2, cols=1, subplot_titles=symbols)

# Add the stock prices and indicators for each symbol to the subplot grid
for i, symbol in enumerate(symbols):
    fig.add_trace(
        go.Scatter(
            x=data[symbol].index,
            y=data[symbol]['Close'],
            name='Price',
            line=dict(color=price_color)
        ),
        row=i+1,
        col=1
    )
    fig.add_trace(
        go.Scatter(
            x=data[symbol].index,
            y=data[symbol]['sma'],
            name=f'{sma_period}-day SMA',
            line=dict(color=sma_color)
        ),
        row=i+1,
        col=1
    )
    fig.add_trace(
        go.Scatter(
            x=data[symbol].index,
            y=data[symbol]['upper_bb'],
            name=f'{bb_period}-day Upper BB',
            line=dict(color=upper_bb_color)
        ),
        row=i+1,
        col=1
    )
    fig.add_trace(
        go.Scatter(
            x=data[symbol].index,
            y=data[symbol]['lower_bb'],
            name=f'{bb_period}-day Lower BB',
            line=dict(color=lower_bb_color)
        ),
        row=i+1,
        col=1
    )
 # Update the layout of the subplot grid
fig.update_layout(
    title='Stock Index Prices',
    height=900,
    width=1000,
)

# Show the plot
fig.show()


# Add the stock prices and indicators for each symbol to the subplot grid
for i, symbol in enumerate(symbols):
    fig.add_trace(
        go.Scatter(
            x=data[symbol].index,
            y=data[symbol]['Close'],
            name='Price',
            line=dict(color=price_color)
        ),
        row=i+1,
        col=1
    )
    fig.add_trace(
        go.Scatter(
            x=data[symbol].index,
            y=data[symbol]['sma'],
            name=f'{sma_period}-day SMA',
            line=dict(color=sma_color)
        ),
        row=i+1,
        col=1
    )
    fig.add_trace(
        go.Scatter(
            x=data[symbol].index,
            y=data[symbol]['upper_bb'],
            name=f'{bb_period}-day Upper BB',
            line=dict(color=upper_bb_color)
        ),
        row=i+1,
        col=1
    )
    fig.add_trace(
        go.Scatter(
            x=data[symbol].index,
            y=data[symbol]['lower_bb'],
            name=f'{bb_period}-day Lower BB',
            line=dict(color=lower_bb_color)
        ),
        row=i+1,
        col=1
    )
    
    # Print the lower, upper and SMA values for the current symbol
    print(f"{symbol}: Lower BB = {data[symbol]['lower_bb'][-1]}, Upper BB = {data[symbol]['upper_bb'][-1]}, SMA = {data[symbol]['sma'][-1]}")
