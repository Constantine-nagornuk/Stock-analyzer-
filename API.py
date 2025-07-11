import yfinance as yf # ignore the red tag doesnt acc do anything
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
About = {}

def drawgraph(frameview, prd , it):
    Stock_Choice = "TSLA" # allow this to also be a input through the GUI portion instead of being static
    STOCK = yf.Ticker(Stock_Choice)
    period = prd
    iterval = it
    def General_Info(Input):
        About["Industry"] = Input["industry"]
        About["quoteType"] = Input["quoteType"]
        About["averageAnalystRating"] = Input["averageAnalystRating"] # 1-5 scale, lower is strong sell, higher is stogng buy 
        About["auditRisk"] = Input["auditRisk"] # % of risk basiclly
        About["shareHolderRightsRisk"] = Input["shareHolderRightsRisk"] # 1-10 scale higher number  = more risk
        About["tradeable"] = Input["tradeable"]
        About["totalDebt"] = Input["totalDebt"]
        About["Stock"] = Input["regularMarketPreviousClose"]
    General_Info(STOCK.info)



    Data = STOCK.history(period=period, interval=iterval)
    StockPrice = Data['Close']
   

    fig, ax = plt.subplots(figsize=(8, 5.5))
    fig.subplots_adjust(right=0.75)
    fig.subplots_adjust(bottom=0.35)
    ax.plot(StockPrice, label="Price", color='blue')
    ax.axhline(y=StockPrice.iloc[0], color='green', linestyle='--', label=f'First Close (${StockPrice.iloc[0]:.2f})')
    ax.axhline(y=StockPrice.iloc[-1], color='red', linestyle='--', label=f'Last Close (${StockPrice.iloc[-1]:.2f})')
    ax.set_title(f"{Stock_Choice} Price Trend — {period} ({iterval} intervals)", fontsize=14)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Stock Price (USD)", fontsize=12)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.20), ncol=3, fontsize=10)    
    canvas = FigureCanvasTkAgg(fig, master= frameview)
    fig.autofmt_xdate()
    canvas.draw()
    canvas.get_tk_widget().grid(padx=20, pady=20, sticky="nsew", row=0, column=0, columnspan=2)



# period can be "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", or "max".
# iterval can be "1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", or "3mo".
#  Note: Minute-level data is generally not available for periods exceeding 7 days. 
