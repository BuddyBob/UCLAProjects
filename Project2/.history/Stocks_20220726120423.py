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
PFM = {"Google":113.87,
             "Microsoft":264.24,
             "Tesla":818.21,
             "Li Auto": 36.11,
             "Mercedes":55.45,
             "NIKE":109.28}

risk_rate = (( 1+ .031 ) / (1+ .090)) - 1
stock_i_weight = round(PFM["Google"]/sum(PFM.values()),2)

print(stock_i_weight)
