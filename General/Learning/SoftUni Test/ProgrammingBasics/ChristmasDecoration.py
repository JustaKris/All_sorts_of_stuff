

budget = int(input())

item = input()
totalValue = 0
while item != "Stop":
    itemValue = 0
    for letter in item:
        itemValue += ord(letter)
    if itemValue <= budget:
        budget -= itemValue
        print("Item successfully purchased!")
    else:
        print("Not enough money!")
        break
    item = input()

if item == "Stop":
    print(f"Money left: {budget}")