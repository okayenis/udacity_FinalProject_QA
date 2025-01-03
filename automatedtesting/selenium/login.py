#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def login(user, password):
    print("Starting the browser...")
    
    # Configure Chromium options
    options = ChromeOptions()
    options.add_argument("--headless")  # Run Chromium in headless mode
    options.add_argument("--no-sandbox")  # Disable sandboxing
    options.add_argument("--disable-dev-shm-usage")  # Use shared memory
    options.add_argument("--disable-gpu")  # Disable GPU rendering
    options.add_argument("--disable-extensions")  # Disable extensions
    options.add_argument("--disable-software-rasterizer")  # Disable software rasterizer
    options.add_argument("--remote-debugging-port=9222")  # Allow remote debugging

    # Specify the binary location for Chromium
    options.binary_location = "/usr/bin/chromium-browser"

    # Use ChromiumDriver explicitly
    driver = webdriver.Chrome(options=options)
    print("Browser started successfully. Navigating to the demo page to login.")
    
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys(user)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("id", "login-button").click()
    print("Login successful.")
    return driver
