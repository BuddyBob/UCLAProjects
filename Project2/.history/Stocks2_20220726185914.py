import pandas as pd
import pandas_datareader.data as web

stock_list = ['AAPL', 'AMZN', 'TSLA']
all_data = {ticker: web.get_data_yahoo(ticker).head(5) for ticker in stock_list}

#portfolio
PFM = pd.DataFrame({ticker: data['Adj Close']
                     for ticker, data in all_data.items()})

#portfolio value
portfolio_value = sum([PFM[i][0] for i in PFM])

#add stock weight column to portfolio
for i in stock_list:
    PFM["Weight"]=PFM[i][0]/portfolio_value
print(PFM)
    


    
 