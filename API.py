import yfinance as yf # ignore the red tag doesnt acc do anything
import pandas as pd
import matplotlib.pyplot as plt 


Stock_Choice = "TSLA"
STOCK = yf.Ticker(Stock_Choice)



def General_Info(Input):
    About = {}
    About["Industry"] = Input["Industry"]
    print(About)
# didnt finihs this something error
General_Info(STOCK.info)




Data = STOCK.history(period="1y", interval="1d")
Data = Data.drop(columns=['Dividends','Stock Splits'])


print((Data))


Data.plot(subplots=True)
plt.show()