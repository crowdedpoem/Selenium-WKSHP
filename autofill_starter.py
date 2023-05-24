from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#Initializes the chrome webdriver into a variable
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#opens the URL path that is specified
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
driver.implicitly_wait(20)
#Maximizes the window
driver.maximize_window()
#Finds the HTML element for the first name bar using the ID

#Sends FirstName in the first name bar

#Finds the HTML elements for last_name, telephone no, email, password and filled them in the same way

#checks the subscribe to newsletter box and clicks

#Checks the terms and conditions box and clicks 

#Finds the continue button and clicks

#Checks what the driver title is after the user has been logged in

#Asserts for successful login 
