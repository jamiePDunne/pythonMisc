import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

rollingWindow=50
zlag=4

# Define function to calculate Z-Score
def zscore(x):
    return (x[-1] - x.mean()) / x.std()

# Retrieve data from Yahoo Finance API
start_date = pd.Timestamp.today() - pd.DateOffset(years=2)
end_date = pd.Timestamp.today()

gdaxi = yf.download("BTC-USD", start=start_date, end=end_date)

# Calculate 50-day Z-Score and lagged Z-Score
rolling_mean = gdaxi["Close"].rolling(window=rollingWindow).mean()
rolling_std = gdaxi["Close"].rolling(window=rollingWindow).std()
z_score = (gdaxi["Close"] - rolling_mean) / rolling_std
z_score_lagged = z_score.shift(zlag)

# Create subplot figure
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add close data trace to subplot
fig.add_trace(
    go.Scatter(x=gdaxi.index, y=gdaxi["Close"], name="Close", hovertemplate="%{x|%Y-%m-%d}<br>Close: %{y:.2f}<extra></extra>"),
    secondary_y=False
)

# Add Z-Score data trace to subplot
fig.add_trace(
    go.Scatter(x=z_score.index, y=z_score, name="Z-Score", hovertemplate="%{x|%Y-%m-%d}<br>Z-Score: %{y:.2f}<extra></extra>"),
    secondary_y=True
)

# Add lagged Z-Score data trace to subplot
fig.add_trace(
    go.Scatter(x=z_score_lagged.index, y=z_score_lagged, name="Z-Score Lagged", hovertemplate="%{x|%Y-%m-%d}<br>Z-Score Lagged: %{y:.2f}<extra></extra>"),
    secondary_y=True
)

# Add zero line to Z-Score y-axis
fig.update_yaxes(
    range=[-4, 4],
    secondary_y=True,
    zeroline=True,
    zerolinecolor="red",
    zerolinewidth=1
)

# Configure layout
fig.update_layout(
    title="BTC-USD Performance and Z-Score",
    xaxis_title="Date",
    yaxis_title="Close",
    yaxis2_title="Z-Score",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    margin=dict(l=50, r=50, t=50, b=50),
    height=600
)

# Add crosshair and format hovermode
fig.update_layout(
    xaxis=dict(
        showspikes=True,
        spikecolor="grey",
        spikemode="across",
        spikethickness=1,
        spikedash="dot",
        rangeslider=dict(visible=True),
        hoverformat="%Y-%m-%d"
    ),
    yaxis=dict(
        showspikes=True,
        spikecolor="grey",
        spikemode="across",
        spikethickness=1,
        spikedash="dot",
        hoverformat=".2f"
    ),
    hovermode="x unified"
)

# Show figure
fig.show() 
