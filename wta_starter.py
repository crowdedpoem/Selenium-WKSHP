# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.espn.com/tennis/")
# allow page to load
driver.implicitly_wait(10)
# maximize window
browser.maximize_window()
# find by tennis rankings link

# click on link

# click on 'Women' link

# locate table on website


# grab table headers

# get the top 10 rows

# go through each row in cell table
