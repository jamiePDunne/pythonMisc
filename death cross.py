import matplotlib.pyplot as plt

start = '2015-01-23'
end = '2022-10-14'

btc = yf.download("BTC-USD", start=start, end=end)

# simple moving averages
btc["50_sma"] = btc["Close"].rolling(50).mean()
btc["200_sma"] = btc["Close"].rolling(200).mean()

# This ensures both SMA start from the same point.
btc = btc.dropna() 
# calcualte death cross
btc["death_x"] = btc.apply(lambda row: 1 if row[f"50_sma"] < row[f"200_sma"]  else 0, axis=1)

# store triggered death crosses 
list_death_x_ts = []
first_death_x = False

# date where the first 50 SMA < 200 SMA is triggered
for idx, each in btc["death_x"].iteritems():
    if each == 1:
        # the first death cross timestamp
        if first_death_x:
            list_death_x_ts.append(idx)
            first_death_x = False
    else:
        first_death_x = True

# plot Death Cross dates
fig, axes = plt.subplots(1,1, figsize=(10,5))
btc[["200_sma","50_sma","Close"]].plot(figsize=(8,4), grid=True, title="SMA 50/200 BTC_USD", ax=axes)

for each in list_death_x_ts:
    axes.axvline(x=each, label="Death X", c="black")
    
axes.legend()
fig.tight_layout()
