Tried downloading files from selenium while crawling websites, didn't work, instead found a way to download files using the installation path of browsers in python.

1. While crawling websites in Selenium, simply create a .txt file in append mode and write the download url of each file in that txt.
2. Once the txt file is completed and contain all links. Type this is the chrome browser chrome://settings/content/pdfDocuments and select the Download PDFs option.
3. Now, head over to chrome://settings/downloads in the browser and change location to designated location and untoggle the rest two options.
4. Install packages from requirements.txt.
5. Check the python code in the same repository for the downloading part.
6. Remember to change time.sleep(1) to suitable seconds, otherwise system will hang and then crash.
