import pyautogui, os
pyautogui.FAILSAFE = True

def GSE_Login():
    # Opening GSE trough Windows search bar
    pyautogui.PAUSE = 0.5
    pyautogui.click(72, 1059)
    pyautogui.typewrite('GfK StarTrack Explorer')
    pyautogui.PAUSE = 10
    pyautogui.press('enter')
    # Username
    pyautogui.PAUSE = 0.2
    pyautogui.doubleClick(973, 524)
    pyautogui.typewrite(os.environ.get('GSE_USER'))
    # Password
    pyautogui.PAUSE = 0.2
    pyautogui.doubleClick(1000, 551)
    pyautogui.typewrite(os.environ.get('GSE_PASS'))
    # Click OK
    pyautogui.PAUSE = 10
    pyautogui.click(992, 588)
    pyautogui.PAUSE = 0.1

# GSE_Login()


def DWH_Login():
    # Opening DWH trough Windows search bar
    pyautogui.PAUSE = 0.5
    pyautogui.click(72, 1059)
    pyautogui.typewrite('GfK DataWarehouse Suite')
    pyautogui.PAUSE = 3
    pyautogui.press('enter')
    # Username
    pyautogui.PAUSE = 0.1
    pyautogui.doubleClick(958, 634)
    pyautogui.typewrite(os.environ.get('GSE_USER'))
    # Password
    pyautogui.doubleClick(987, 669)
    pyautogui.typewrite(os.environ.get('GSE_PASS'))
    # Click OK
    pyautogui.PAUSE = 12
    pyautogui.click(1047, 712)

def BTT_Export_Lists():
    # Select Batch to target
    pyautogui.PAUSE = 0.5
    pyautogui.click(16, 34)
    pyautogui.click(43, 52)
    pyautogui.click(173, 122)
    pyautogui.click(887, 616)
    # Wait to load
    pyautogui.PAUSE = 4
    pyautogui.click(935, 814)
    pyautogui.PAUSE = 1
    # Window -> Cascade
    pyautogui.PAUSE = 0.5
    pyautogui.click(58, 32)
    pyautogui.click(97, 54)
    # Refresh
    pyautogui.click(68, 96)
    pyautogui.PAUSE = 3
    pyautogui.click(1374, 680)
    pyautogui.PAUSE = 0.1

# DWH_Login()