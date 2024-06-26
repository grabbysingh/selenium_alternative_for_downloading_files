import time
import webbrowser
import pyautogui

# Path to the Chrome executable
chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'

# Create webbrowser object
webbrowser_obj = webbrowser.get(chrome_path)

page_link = ''

for indx in range(468):
	
	webbrowser_obj.open(page_link+str(indx+1))
	time.sleep(3)
	pyautogui.hotkey('ctrl', 's')
	time.sleep(1)
	pyautogui.press('enter')

	print('webpages downloaded =', indx+1)