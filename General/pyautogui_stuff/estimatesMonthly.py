import pyautogui

pyautogui.FAILSAFE = True

# Input
releaseKey = str(input('Release Key: '))
# releaseKey = str(759)
startingMonth = str(input('Starting Month: '))
# startingMonth = str(8)
endingMonth = str(input('Ending Month: '))
# endingMonth = str(9)


# Open MS SQL Server
pyautogui.PAUSE = 30
pyautogui.doubleClick(2538, 1061)  # Icon
#pyautogui_stuff.PAUSE = 0.1
pyautogui.PAUSE = 5
pyautogui.doubleClick(2819, 552)  # Connect
pyautogui.PAUSE = 1
pyautogui.click(1939, 39)  # File
pyautogui.click(2016, 133)  # Open
pyautogui.PAUSE = 3
pyautogui.click(2305, 206)  # File
pyautogui.doubleClick(2411, 497)  # Select query

# Editing query Release key
pyautogui.PAUSE = 0.3
pyautogui.doubleClick(2490, 227)
pyautogui.typewrite(str(releaseKey))
# Editing query period
pyautogui.click(2668, 227)  # From period
for i in range(0, len(startingMonth)):
    pyautogui.press('backspace')
pyautogui.typewrite(startingMonth)
pyautogui.click(3138, 228)  # To period
for i in range(0, len(str(endingMonth))):
    pyautogui.press('backspace')
pyautogui.typewrite(str(endingMonth))
pyautogui.PAUSE = 5
pyautogui.click(2201, 87)  # Execute click

# Copy the data
pyautogui.PAUSE = 0.5
pyautogui.click(2367, 608)
pyautogui.click(2367, 608, button='right')
pyautogui.moveTo(2445, 645)
pyautogui.click(2445, 645)

# Opening Excel trough Windows search bar
pyautogui.PAUSE = 0.5
pyautogui.click(1990, 1057)
pyautogui.typewrite('Excel')
pyautogui.PAUSE = 10
pyautogui.press('enter')

# Creating pivot
pyautogui.PAUSE = 1.5
pyautogui.hotkey('ctrl', 'v')  # paste
pyautogui.doubleClick(148, 49)  # Insert
pyautogui.click(34, 86)  # Pivot Table
pyautogui.click(1012, 600)  # OK
# Pivot
pyautogui.PAUSE = 0.5
pyautogui.click(1592, 416)  # Country
pyautogui.click(1592, 435, button='right')  # Period
pyautogui.click(1693, 445)
pyautogui.click(1592, 453)  # ReportingChannel
pyautogui.click(1592, 471)  # DistributionType
pyautogui.click(1592, 491)  # Segment
pyautogui.click(1592, 512)  # uMoM
pyautogui.click(1592, 526)  # vMoM
# Changing sum to average
pyautogui.click(1845, 862)
pyautogui.click(1845, 839)
pyautogui.doubleClick(807, 493)

pyautogui.click(1845, 883)
pyautogui.click(1845, 860)
pyautogui.doubleClick(807, 493)
# Design tab
pyautogui.click(805, 46)  # Design
pyautogui.click(38, 84)  # Subtotals
pyautogui.click(120, 164)
pyautogui.click(133, 96)  # Report Layout
pyautogui.click(220, 300)  # Repeat All Item Labels
pyautogui.click(133, 96)  # Report Layout
pyautogui.click(215, 251)  # Show in Tabular Form



