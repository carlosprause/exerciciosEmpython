km = float(input('how many kilometers did this car cover?'))
days = int(input('how many days was this car rented?'))
priceForkm = km * 0.15
priceForDay = days * 60
priceAll = priceForkm + priceForDay
print('This car cover {} km and rented for {:.0f} days! The price of pay is: {:.2f}'.format(km, days, priceAll))