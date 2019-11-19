import pyautogui, os
from General.pyautogui_stuff import GSE_DWH_Login

pyautogui.FAILSAFE = True


# GSE_DWH_Login.DWH_Login()
#
# # Tablet weekly
# pyautogui.PAUSE = 0.5
# pyautogui.click(134, 307)
# pyautogui.click(71, 640)


missing = input("Enter missing countries: ")

scrollMid = -450
scrollBottom = -1000

countryDict = {
    "Argentina": [500, 300, 0],
    "Australia": [12, 14, 3],
    "GB": [12, 14, 3, "Brao!"],
    "Ukraine": [111, 111, scrollBottom],
    "UAE": [222, 222, scrollBottom]

}

try:
    countryDict["GB"][3]
except:
    pass
else:
    print(countryDict["GB"][3])

# missing = "Argentina Belarus UAEUkraine"


confirmedMissing = []
for i in countryDict:
    if i in missing:
        confirmedMissing.append(i)

print(confirmedMissing)

for i in confirmedMissing:
    countryDict.pop(i)

for i in countryDict:
    # print(countryList[i])
    x, y, scroll = countryDict[i]
    print(x, y, scroll)

# pyautogui.PAUSE = 0.3
# pyautogui.moveTo(185, 511)
# pyautogui.scroll(1450)
# pyautogui.scroll(-450)
# # pyautogui.scroll(-1000)


