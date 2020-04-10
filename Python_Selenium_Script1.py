from time import sleep
import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from PIL import Image
import requests
import re  
options = Options()
#options.add_argument('C:\\chromedriver.exe')
options.add_argument('--headless')
options.add_argument(f"--window-size=850,2000")
path = "C:\\chromedriver.exe"
driver=webdriver.Chrome(path,options=options)
driver.set_page_load_timeout(50)
driver.get('http://google.com')

# Image Crop Dimensions
x = 265  #X location in px where cropping would start
y = 1100 #Y location in px where cropping would start
width = 470 #Width of cropped image
height = 350 #Height of cropped image
n_times = 5 # number of screenshots
img_interval = 10 #interval between two iamges in seconds

for i in range(n_times):
    date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S") 
    screenshotN = "C:\\WebTimelapse\\"+"myfile"+ date + ".png"
    driver.save_screenshot(screenshotN)
    img = Image.open(screenshotN) 
    #img = img.crop( ( x, y, x + width , y + height ) )
    img.save(screenshotN)
    print(date)
    sleep(img_interval)
driver.quit()
