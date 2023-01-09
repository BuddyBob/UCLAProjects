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
#113.87
#264.24
#818.21

PFM = {
        "Google": { "num_shares":1000, "per_share": 10 },
        "Microsoft": { "num_shares":4000,"per_share":20 },
        "Tesla": { "num_shares":2000,"per_share":5 }
    }

risk_rate = (( 1+ .031 ) / (1+ .090)) - 1

portfolio_value = sum([v["per_share"]*v["num_shares"] for v in PFM.values()])

stock_i = PFM["Google"]
stock_i_weight = stock_i["per_share"]*stock_i["num_shares"]/portfolio_value
print(stock_i_weight)