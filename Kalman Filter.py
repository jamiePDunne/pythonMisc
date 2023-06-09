import yfinance as yf
import numpy as np
import pandas as pd
import plotly.subplots as sp
import plotly.graph_objects as go
from pykalman import KalmanFilter


# Fetch data from yfinance
sindex = yf.download('^gdaxi', start='2020-01-01', end='2021-01-01', progress=False)

# Define the state space model
observation_matrices = np.array([[1, 0]])
transition_matrices = np.array([[1, 1], [0, 1]])
observation_covariance = np.cov(sindex['Close'], ddof=0)
transition_covariance = np.array([[1e-5, 1e-5], [1e-5, 1e-5]])
initial_state_mean = np.array([sindex['Close'][0], 0])
initial_state_covariance = np.eye(2)

# Initialize the Kalman filter
kf = KalmanFilter(
    observation_matrices=observation_matrices,
    transition_matrices=transition_matrices,
    observation_covariance=observation_covariance,
    transition_covariance=transition_covariance,
    initial_state_mean=initial_state_mean,
    initial_state_covariance=initial_state_covariance
)

# Run the Kalman filter
state_means, state_covs = kf.filter(sindex['Close'].values)

# Use the estimated state variables to generate trading signals
sindex['kalman_trend'] = state_means[:, 0]
sindex['sig_kalman'] = np.where(sindex['Close'] > sindex['kalman_trend'], 1, -1)

# Create subplots
fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True)

# Add Close price to the first subplot
fig.add_trace(go.Scatter(x=sindex.index, y=sindex['Close'], name='Close Price'), row=1, col=1)

# Add Kalman trend to the first subplot
fig.add_trace(go.Scatter(x=sindex.index, y=sindex['kalman_trend'], name='Kalman Trend'), row=1, col=1)

# Add signal to the second subplot
fig.add_trace(go.Scatter(x=sindex.index, y=sindex['sig_kalman'], name='Signal (Kalman)'), row=2, col=1)

# Update subplot titles and axis labels
fig.update_layout(
    title='^GDAXI Price Data with Kalman Filter Signal',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Price'),
    yaxis2=dict(title='Signal')
)

# Show the plot
fig.show()
