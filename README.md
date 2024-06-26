# Common settings to be changed before moving to python codes.

1. Type this is the chrome browser chrome://settings/content/pdfDocuments and select the Download PDFs option.
2. Now, head over to chrome://settings/downloads in the browser and change location to designated location and untoggle the rest two options.
3. Install packages from requirements.txt.

# Tried downloading files from selenium while crawling websites, didn't work, instead found a way to download files using the installation path of browsers in python.

1. While crawling websites in Selenium, simply create a .txt file in append mode and write the download url of each file in that txt.
2. Check the python code named as download_files.py in the same repository for the downloading part.
3. Remember to change time.sleep(1) to suitable seconds, otherwise system will hang and then crash.

# On some webpages driver.get('webpage') and requests.get('webpage') doesn't work. Basically, automate the process of downloading those webpages as .html file and load them in python for further retrieval of data from those pages.

1. Check the python code named as download_webpages.py in the same repository for downloading the webpages.
2. Remember to change the multiple time.sleep() used to suitable seconds, otherwise system will hang and then crash.
