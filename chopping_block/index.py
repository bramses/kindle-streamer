import pyautogui
import pygetwindow as gw

windows = gw.getAllTitles()
# print methods in gw
print(dir(gw))

# Find the window you want to capture
kindle_windows = gw.getWindowsWithTitle('Kindle')[0]
if kindle_windows:
    window = kindle_windows[0]
    # Bring the window to the foreground
    window.activate()
    # Wait a moment for the window to be active
    pyautogui.sleep(2)
    # Capture the window area
    screenshot = pyautogui.screenshot(region=window.box)
    screenshot.save('window_screenshot.png')

# Find the window you want to capture
# kindle_windows = [window for window in windows if 'Kindle' in window]
# if kindle_windows:
#     window = kindle_windows[0]
#     # Bring the window to the foreground
#     window.activate()
#     # Wait a moment for the window to be active
#     pyautogui.sleep(2)
#     # Capture the window area
#     screenshot = pyautogui.screenshot(region=window.box)
#     screenshot.save('window_screenshot.png')
