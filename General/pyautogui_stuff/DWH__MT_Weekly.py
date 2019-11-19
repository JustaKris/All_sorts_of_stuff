import pyautogui, os
from General.pyautogui_stuff import GSE_DWH_Login

pyautogui.FAILSAFE = True

# Inputs
# Current or previous period
periodInput = input('Enter "c" for current period or "p" for previous period\n||Period -----> ')
while "c" not in periodInput.lower() and "p" not in periodInput.lower():
    print("Try again!")
    periodInput = input('Enter "c" for current period or "p" for previous period\n||Period -----> ')
# Country
countryInput = input("Enter missing countries\n||Countries --> ")
# Action
addOrRemove = input('To select only the given countries type "select", to remove only the given countries type "remove"\n||Action -----> ')
while "select" not in addOrRemove and "remove" not in addOrRemove:
    print("Try again!")
    addOrRemove = input('To select only the given countries type "select", to remove only the given countries type "remove"\n||Action -----> ')

# Login and navigation to BTT menu
GSE_DWH_Login.DWH_Login()
GSE_DWH_Login.BTT_Export_Lists()

# Tablet weekly
pyautogui.PAUSE = 0.5
pyautogui.click(134, 307)

# Select/Deselect all
if "remove" in addOrRemove.lower():
    pyautogui.click(71, 640)  # Select all -> use to make script deselect only the given countries
elif "select" in addOrRemove.lower():
    pyautogui.click(154, 641)  # Deselect all -> use to make script select only the given countries


scrollTop = 1450
scrollMid = -450
scrollBottom = -1000

# List of available countries
countryDict = {
    "Argentina": [41, 467],
    "Australia": [41, 486],
    "Austria": [41, 502],
    "Belgium": [41, 518],
    "Chile": [41, 538],
    "Colombia": [41, 552],
    "Denmark": [41, 569],
    "Finland": [41, 588],
    "France": [41, 605],
    "Germany": [41, 467, scrollMid],
    "GB": [41, 486, scrollMid],
    "HK": [41, 502, scrollMid],
    "Italy": [41, 518, scrollMid],
    "Japan": [41, 538, scrollMid],
    "Kazakhstan": [41, 552, scrollMid],
    "Netherlands": [41, 569, scrollMid],
    "Peru": [41, 588, scrollMid],
    "Poland": [41, 605, scrollMid],
    "Portugal": [41, 486, scrollBottom],
    "Russia": [41, 502, scrollBottom],
    "Spain": [41, 518, scrollBottom],
    "Sweden": [41, 538, scrollBottom],
    "Switzerland": [41, 552, scrollBottom],
    "Turkey": [41, 569, scrollBottom],
    "Ukraine": [41, 603, scrollBottom],
    "UAE": [41, 586, scrollBottom]
}

# Can't change a dict that is being iterated, had to improvise
confirmedMissing = []
for i in countryDict:
    if i.lower() in countryInput.lower():
        confirmedMissing.append(i)

# Iterating trough the given Countries
pyautogui.PAUSE = 0.2
pyautogui.moveTo(328, 532)
pyautogui.scroll(scrollTop)
previousScroll = 0
for i in confirmedMissing:
    if i in countryDict:
        try:
            countryDict[i][2]
        except IndexError:
            x, y = countryDict[i]
            pyautogui.click(x, y)
        else:
            x, y, scroll = countryDict[i]
            if previousScroll == scroll:
                pyautogui.click(x, y)
            else:
                pyautogui.scroll(scroll)
                pyautogui.click(x, y)
                # if scroll != previousScroll:
                #     previousScroll = scroll
                previousScroll = scroll

# Export
pyautogui.PAUSE = 4
pyautogui.click(1539, 639)

# Click current period
pyautogui.PAUSE = 0.3
if periodInput.lower() == "c":
    pyautogui.doubleClick(595, 210)
elif periodInput.lower() == "p":
    pyautogui.doubleClick(595, 225)  # Previous period


# pyautogui.doubleClick(595, 210)  # OK






