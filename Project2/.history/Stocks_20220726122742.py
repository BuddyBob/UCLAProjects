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
        "Google": { "num_shares":100, "per_share": 113.87 },
        "Microsoft": { "num_shares":80,"per_share":264.24 },
        "Tesla": { "num_shares":100,"per_share":818.21 }
    }

risk_rate = (( 1+ .031 ) / (1+ .090)) - 1

portfolio_value = sum([v["per_share"]*v["num_shares"] for v in PFM.values()])
stock_i = PFM["Google"]
stock_i_weight = round(stock_i["per_share"]*stock_i["num_shares"]/portfolio_value,2)

print(stock_i_weight)