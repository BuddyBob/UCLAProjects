import pandas as pd
import pandas_datareader.data as web

stock_list = ['AAPL', 'AMZN', 'TSLA']
all_data = {ticker: web.get_data_yahoo(ticker).head(5) for ticker in stock_list}
print(all_data)

#portfolio
P = pd.DataFrame({ticker: data['Adj Close']
                     for ticker, data in all_data.items(
                         
print(P)