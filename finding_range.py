index_price = float(input("Please enter the current price of Index: "))
vix = float(input("Please enter the value of India Vix : "))

print("\t")

print("Probalility of Index going up and down annually is, ","-",vix,"to","+",vix)

annually_high = index_price +  (index_price * vix/100)
print("Annually  High:",annually_high)

annually_low = index_price - (index_price * vix/100)
print("Annually Low:",annually_low)

print('\t')

prob_monthly = vix/pow(12,1/2)
print("Probalility of Index going up and down monthly is, ","-",prob_monthly,"to","+",prob_monthly)

monthly_high = index_price + (index_price * prob_monthly/100)
print("Monthly High: ",monthly_high)

monthly_low = index_price - (index_price * prob_monthly/100)
print("Monthly Low: ",monthly_low)

print('\t')

prob_weekly = vix/pow(52,1/2)
print("Probalility of Index going up and down weekly is, ","-",prob_weekly,"to","+",prob_weekly)

weekly_high = index_price + (index_price * prob_weekly/100)
print("Weekly High: ",weekly_high)

weekly_low = index_price - (index_price * prob_weekly/100)
print("Weekly Low: ",weekly_low)

print('\t')

prob_daily = vix/pow(365,1/2)
print("Probalility of Index going up and down daily is, ","-",prob_daily,"to","+",prob_daily)

day_high = index_price + (index_price * prob_daily/100)
print("Day High: ",day_high)

day_low = index_price - (index_price * prob_daily/100)
print("Day Low: ",day_low)

print('\t')
print('\t')

print("Created By: Pratham Sharma")
print("GitHub: https://github.com/virtualpratham")
