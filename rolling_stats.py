import exercise1 as ex
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('2012-01-01', '2012-12-31')
symbols = ['SPY']
df = ex.get_data(symbols, dates)

ax = df['SPY'].plot(title="SPY Rolling Mean", label='SPY')

# 20-day rolling mean
# Deprecated Version : rm_SPY = pd.rolling_mean(df['SPY'], window=20)
rm_SPY = df['SPY'].rolling(window=20).mean()

rm_SPY.plot(label='Rolling Mean SPY', ax=ax)
plt.show()
