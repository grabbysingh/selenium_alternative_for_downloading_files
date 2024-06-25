import time
import webbrowser

# Path to the Chrome executable
chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'

# Create webbrowser object
webbrowser_obj = webbrowser.get(chrome_path)

# Path to the .txt file
pth_txt_file = "all_pdf_links.txt"

with open(pth_txt_file, 'r') as f:
	lst_links = f.readlines()

for indx, url in enumerate(lst_links):

	print("files done =", indx+1)

	# Register the browser and open the URL
	webbrowser_obj.open(url)
	time.sleep(1)
