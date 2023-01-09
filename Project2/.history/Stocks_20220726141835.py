"""
Date: Jul 25 2022

Portfolio:

## Tech
- Alphabet Inc. (GOOGL) - ADJ CLOSE: 108.21	
- Microsoft Corporation (MSFT) - ADJ CLOSE: 258.83	


## Car Market
- Tesla, Inc. (TSLA) - ADJ CLOSE: 805.30		
- Mercedes-Benz Group AG (MBG.DE) - ADJ CLOSE: 55.45		
- Li Auto Inc. (LI) - ADJ CLOSE: 34.60		

##Other
- NIKE, Inc. (NKE) - ADJ CLOSE: 109.28	
"""
#portfolio
PFM = {
        "Google": { "num_shares":10000, "per_share": 10 },
        "Microsoft": { "num_shares":80,"per_share":264.24 },
        "Tesla": { "num_shares":120,"per_share":818.21 }
    }

#Risk-free Rate of Return = ( 1+Governmennt Bond Rate1+Inflation rate) – 1
#https://wealthface.com/blog/risk-free-rate/#:~:text=The%20value%20of%20a%20risk,risk%2Dfree%20rate%20of%20return.
risk_rate = (( 1+ .031 ) / (1+ .090)) - 1

#stock value (price per share * num_shares) / portfolio_value (sum of all stock values)
portfolio_value = sum([v["per_share"]*v["num_shares"] for v in PFM.values()])
stock_i = PFM["Google"]
stock_i_weight = round(stock_i["per_share"]*stock_i["num_shares"]/portfolio_value,2)


#ROI
#(current_value-cost_of_investment)/cost_of_investment
ROI = (stock_i["num_shares"]*stock_i["per_share"]-2500)/2500
print("Expected return:", ROI)
#Standard Deviation

