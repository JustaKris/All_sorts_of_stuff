

guestSum = int(input())

command = input()
totalIncome = 0
totalGuests = 0
while command != "The restaurant is full":
    groupSize = int(command)
    if groupSize < 5:
        couvert = 100
    else:
        couvert = 70

    totalGuests += groupSize
    totalIncome += couvert * groupSize

    command = input()

if totalIncome >= guestSum:
    # print("You have %d guasts and %.2f leva left." % totalGuests, totalIncome - guestSum)
    print(f'You have {totalGuests} guests and {totalIncome - guestSum} leva left.')
else:
    print(f'You have {totalGuests} guests and {totalIncome} leva income, but no singer.')