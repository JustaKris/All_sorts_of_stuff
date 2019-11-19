import pyautogui, os
from General.pyautogui_stuff import GSE_DWH_Login

pyautogui.FAILSAFE = True


countryInput = input("Enter missing countries: ")

scrollTop = 1450
scrollMid = -450
scrollBottom = -1000

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

confirmedMissing = []
for i in countryDict:
    if i in countryInput:
        confirmedMissing.append(i)


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
                if scroll != previousScroll:
                    previousScroll = scroll
