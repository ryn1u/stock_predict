from dateutils import get_workday, get_day
import yfinance as yf
import pandas

name = "MSFT"
msft = yf.Ticker(name)

hist = msft.history("5d", "5m")

print(hist)
print()
print(type(hist))

for (index, series) in hist.iterrows():
    print(index)
    print(series)