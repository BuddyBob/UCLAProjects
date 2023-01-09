import pandas as pd
import pandas_datareader.data as web

stock_list = ['AAPL', 'AMZN', 'TSLA']
all_data = {ticker: web.get_data_yahoo(ticker).head(5) for ticker in stock_list}

for i in all_data:
    print(i)

#portfolio value
portfolio_value = sum([PFM[i][0] for i in PFM])




    
 