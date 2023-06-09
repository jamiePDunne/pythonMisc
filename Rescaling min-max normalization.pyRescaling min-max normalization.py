import matplotlib.pyplot as plt
from datetime import date
%matplotlib inline

import yfinance as yf
today = date.today()
start = '2020-01-26'
index = yf.download("btc-usd", start=start, end=today)

////

rollingDays=50

plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (20, 5)

index['Close'].plot(label = 'CLOSE', color = 'blue')

plt.legend(loc = 'upper right')
plt.title('Index RAW price')
plt.show()

//

maxi = index['Close'].rolling(rollingDays).max()
mini = index['Close'].rolling(rollingDays).min()

index['norm'] = (index['Close']-mini)/(maxi-mini)

index['norm'].plot(label = 'norm', color = 'blue')

plt.legend(loc = 'upper left')
plt.title('Index min max transformed price')
plt.show()
