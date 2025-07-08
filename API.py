import yfinance as yf # ignore the red tag doesnt acc do anything
import pandas as pd
import matplotlib.pyplot as plt 


Stock_Choice = "TSLA"
STOCK = yf.Ticker(Stock_Choice)



def General_Info(Input):
    About = {}
    About["Industry"] = Input["industry"]
    About["quoteType"] = Input["quoteType"]
    About["averageAnalystRating"] = Input["averageAnalystRating"] # 1-5 scale, lower is strong sell, higher is stogng buy 
    About["auditRisk"] = Input["auditRisk"] # % of risk basiclly
    About["shareHolderRightsRisk"] = Input["shareHolderRightsRisk"] # 1-10 scale higher number  = more risk
    About["tradeable"] = Input["tradeable"]
    About["totalDebt"] = Input["totalDebt"]

    print(About)

General_Info(STOCK.info)



# period can be "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", or "max".
# iterval can be "1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", or "3mo".
#  Note: Minute-level data is generally not available for periods exceeding 7 days. 

Data = STOCK.history(period="1y", interval="1d")

Data = Data.drop(columns=['Dividends','Stock Splits'])
Day_Open_Price = Data["Open"]
Day_High_Price = Data["High"]
Day_Low_Price = Data["Low"]
Day_Close_Price = Data["Close"]
Day_Volume_Price = Data["Volume"]






""" Data.plot(subplots=True)
plt.show() """