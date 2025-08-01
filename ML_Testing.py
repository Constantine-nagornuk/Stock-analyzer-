import mplfinance as mpf
import API
import yfinance as yf # ignore the red tag doesnt acc do anything
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import os
from PIL import Image



Stock_Choice = "URI"
STOCK = yf.Ticker(Stock_Choice)
Data = STOCK.history(period="1mo", interval="1d")
Data = Data.drop(columns=['Dividends','Stock Splits'])
Data.index = pd.to_datetime(Data.index.date)






DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")
filename = os.path.join(DOWNLOADS, f"{Stock_Choice}_candlestick.png")
mpf.plot(
    Data,
    type='candle',
    style='yahoo',
    savefig=filename
)











#https://github.com/matplotlib/mplfinance/blob/master/examples/using_lines.ipynb
# allow user to draw diffrent lines with diffrent inputs they want
# allow them to put V or H lines and possibly the other types listed there