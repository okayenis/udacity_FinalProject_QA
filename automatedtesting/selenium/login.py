#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def login(user, password):
    print('Starting the browser...')
    options = ChromeOptions()
    # Uncomment below for headless execution (e.g., in CI/CD pipelines)
    # options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    print('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    # Login
    print(f'Attempting to log in as {user}')
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Verify login
    if "inventory" in driver.current_url:
        print('Login successful!')
    else:
        print('Login failed. Exiting.')
        driver.quit()
        return None

    return driver

def add_all_products_to_cart(driver):
    print('Adding all products to the cart...')
    add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for button in add_buttons:
        print(f'Adding product: {button.get_attribute("id")}')
        button.click()
    print('All products added to the cart.')

def remove_all_products_from_cart(driver):
    print('Removing all products from the cart...')
    remove_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for button in remove_buttons:
        print(f'Removing product: {button.get_attribute("id")}')
        button.click()
    print('All products removed from the cart.')

if __name__ == "__main__":
    driver = login('standard_user', 'secret_sauce')
    if driver:
        add_all_products_to_cart(driver)
        time.sleep(2)  # Just to visually verify the cart if not headless
        remove_all_products_from_cart(driver)
        time.sleep(2)  # Just to visually verify the cart if not headless
        print('Test suite execution complete. Closing browser.')
        driver.quit()
