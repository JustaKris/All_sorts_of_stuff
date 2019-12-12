
priceBaklava = float(input())
priceMuffin = float(input())
shtolen = float(input())
candy = float(input())
cookies = float(input())

priceShtolen = priceBaklava * 1.6
priceCandy = priceMuffin * 1.8
priceCookies = 7.5

totalShtolen = shtolen * priceShtolen
totalCandy = candy * priceCandy
totalCookies = cookies * priceCookies

totalTotal = totalCandy+totalCookies+totalShtolen

print("%.2f" % totalTotal)
print(f'{totalTotal:.2f}')
