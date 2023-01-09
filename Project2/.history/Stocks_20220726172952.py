
import pandas as pd
import pandas_datareader.data as web

stock_list = ['AAPL', 'AMZN', 'TSLA']
all_data = {ticker: web.get_data_yahoo(ticker).head(5) for ticker in stock_list}
print(all_data)

#portfolio
PFM = pd.DataFrame({ticker: data['Adj Close']
                     for ticker, data in all_data.items() })



portfolio_value = sum([v["per_share"]*v["num_shares"] for v in PFM.values()])

li = []
for stock in PFM.keys():
    stock_i = PFM[stock]
    
    #STOCK WEIGHT
    #stock value (price per share * num_shares) / portfolio_value (sum of all stock values)
    stock_i_weight = stock_i["per_share"]*stock_i["num_shares"]/portfolio_value
    print(stock,"stock weight:",stock_i_weight)

    #ROI
    #(current_value-cost_of_investment)/cost_of_investment
    ROI = ((stock_i["num_shares"]*stock_i["per_share"]-2500)/2500)/100
    print(stock,"return:", ROI)
    li.append(stock_i_weight*ROI)

#EXCPECTED PORTFOLIO RETURN
ex_return = sum(li)
print("\n\nexcpected portfolio return",round(ex_return*100,2))
#Risk-free Rate of Return = ( 1+Governmennt Bond Rate1+Inflation rate) – 1
risk_rate = (( 1+ .031 ) / (1+ .090)) - 1
print("risk rate:",round(abs(risk_rate*100),2))
    
    

#Standard Deviation
