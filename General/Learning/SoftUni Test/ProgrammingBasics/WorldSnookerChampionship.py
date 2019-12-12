

championshipStage = input()
ticketType = input()
numberOfTickets = int(input())
photo = input()

price = 0.0

if championshipStage == "Quarter final":
    if ticketType == "Standard":
        price = 55.5
    elif ticketType == "Premium":
        price = 105.2
    else:
        price = 118.90
elif championshipStage == "Semi final":
    if ticketType == "Standard":
        price = 75.88
    elif ticketType == "Premium":
        price = 125.22
    else:
        price = 300.4
else:
    if ticketType == "Standard":
        price = 110.1
    elif ticketType == "Premium":
        price = 160.66
    else:
        price = 400

totalPrice = price * numberOfTickets

freePhoto = False
if totalPrice > 4000:
    totalPrice *= 0.75
    freePhoto = True

elif totalPrice > 2500:
    totalPrice *= 0.9

if photo == "Y" and not freePhoto:
    totalPrice += 40 *numberOfTickets



print("%.2f" % totalPrice)