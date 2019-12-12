import math

goal = float(input())
fantasyBooks = int(input())
horrorBooks = int(input())
romanticBooks = int(input())

fantasyTotal = fantasyBooks * 14.9
horrorTotal = horrorBooks * 9.8
romanticTotal = romanticBooks * 4.3

totalBooks = fantasyTotal + horrorTotal + romanticTotal
totalBooksBezDDS = totalBooks * 0.8

sellersReceive = math.floor((totalBooksBezDDS - goal) * 0.1)

if totalBooksBezDDS >= goal:
    print("%.2f leva donated." % (totalBooksBezDDS - sellersReceive))
    print("Sellers will receive %.0f leva." % sellersReceive)
else:
    print("%.2f money needed." % (goal - totalBooksBezDDS))
