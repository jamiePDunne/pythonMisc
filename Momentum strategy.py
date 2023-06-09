mport pandas as pd
import yfinance as yf
import plotly.graph_objs as go

# Download historical data for the s&p 500 from Yahoo Finance
data = yf.download("^GSPC", start="2020-01-01", end="2023-01-01")

# Calculate the 50-day momentum
data['Momentum'] = data['Close'] - data['Close'].shift(50)

# Momentum strategy: Buy when the 50-day momentum is positive
# Create a new column called "Momentum Signal" and initialize it to 0
data['Momentum Signal'] = 0
# Set the values of the "Momentum Signal" column to 1 when the 50-day momentum is positive
data.loc[data['Momentum'] > 0, 'Momentum Signal'] = 1

# Calculate returns based on the signals
# Calculate the daily returns of the closing price
daily_returns = data['Close'].pct_change()
# Shift the signals by one day to align them with the returns
momentum_signal_shifted = data['Momentum Signal'].shift(1)
# Calculate the returns for the momentum strategy by multiplying the daily returns by the momentum signal
data['Momentum Returns'] = daily_returns * momentum_signal_shifted

# Calculate cumulative returns
data['Momentum Cumulative Returns'] = (1 + data['Momentum Returns']).cumprod()

# Plot the cumulative returns
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Momentum Cumulative Returns'], name='Momentum Cumulative Returns'))
fig.update_layout(title='Momentum Trading Strategy Backtest',
                  xaxis_title='Date',
                  yaxis_title='Cumulative Returns')
fig.show()

# Calculate backtest metrics
total_trades = data['Momentum Signal'].diff().abs().sum() / 2
winning_trades = (data['Momentum Returns'] > 0).sum()
losing_trades = (data['Momentum Returns'] < 0).sum()
win_rate = winning_trades / total_trades
average_win = data.loc[data['Momentum Returns'] > 0, 'Momentum Returns'].mean()
average_loss = data.loc[data['Momentum Returns'] < 0, 'Momentum Returns'].mean()
profit_factor = - average_win / average_loss
total_return = (data['Momentum Cumulative Returns'][-1] - 1) * 100

# Print backtest metrics
print(f"Total Trades: {total_trades}")
print(f"Winning Trades: {winning_trades}")
print(f"Losing Trades: {losing_trades}")
print(f"Win Rate: {win_rate:.2%}")
print(f"Average Win: {average_win:.4f}")
print(f"Average Loss: {average_loss:.4f}")
print(f"Profit Factor: {profit_factor:.2f}")
print(f"Total Return: {total_return:.2f}%")
