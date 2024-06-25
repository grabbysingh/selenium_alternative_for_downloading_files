import time
import webbrowser

with open('all_links.txt', 'r') as f:
	lst_links = f.readlines()

for url in lst_links:

	# Path to the Chrome executable
	chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'

	# Register the browser and open the URL
	webbrowser.get(chrome_path).open(url)
	time.sleep(1)