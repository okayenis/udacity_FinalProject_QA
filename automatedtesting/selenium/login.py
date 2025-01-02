#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login(user, password):
    print("Starting the browser...")
    # --uncomment when running in Azure DevOps.
    # options = ChromeOptions()
    # options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    print("Browser started successfully. Navigating to the demo page to login.")
    driver.get("https://www.saucedemo.com/")

    # Login işlemi
    driver.find_element("id", "user-name").send_keys(user)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("id", "login-button").click()
    print("Login successful.")
    return driver
