#Mouse position
'''
import pyautogui_stuff

print('Press Ctrl-C to quit.')

try:
    while True:

        x, y =pyautogui_stuff.position()
        positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)

        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone.')
'''


# Use in CMD for best results
import pyautogui

pyautogui.displayMousePosition()