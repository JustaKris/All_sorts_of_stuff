import pyautogui
pyautogui.FAILSAFE = True

#StarTrack
#pyautogui.moveTo(507, 1070)
pyautogui.PAUSE = 8
pyautogui.doubleClick(560, 1060)
#Username
pyautogui.PAUSE = 0.1
pyautogui.doubleClick(1000, 530)
pyautogui.typewrite('knbone1')
#Password
pyautogui.doubleClick(1000, 560)
pyautogui.typewrite('Saf5stpa55!!!!')
#Click OK
pyautogui.PAUSE = 10
pyautogui.click(992, 588)
pyautogui.PAUSE = 0.1

#DWH
#pyautogui.moveTo(562, 1070)
pyautogui.PAUSE = 3
pyautogui.doubleClick(607, 1060)
#Username
pyautogui.PAUSE = 0.1
pyautogui.doubleClick(958, 634)
pyautogui.typewrite('knbone1')
#Password
pyautogui.doubleClick(987, 669)
pyautogui.typewrite('Saf5stpa55!!!!')
#Click OK
pyautogui.click(1047, 712)
pyautogui.PAUSE = 12
#Select Batch to target
pyautogui.click(16, 34)
pyautogui.PAUSE = 0.5
pyautogui.click(43, 52)
pyautogui.click(173, 122)
pyautogui.click(887, 616)
#Wait to load
pyautogui.PAUSE = 8
pyautogui.click(935, 814)
pyautogui.PAUSE = 1
#Refresh filter
pyautogui.click(64, 93)
pyautogui.click(945, 682)