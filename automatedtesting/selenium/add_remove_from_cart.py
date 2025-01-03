import logging
import time
from login import login  
from selenium.webdriver.common.by import By


logging.basicConfig(filename="test_suite.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def add_all_products_to_cart(driver):
    print("Adding all products to the cart...")
    logging.info("Adding all products to the cart.")
    items = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for idx, item in enumerate(items, start=1):
        item.click()
        print(f"Product {idx} added to the cart.")
        logging.info(f"Product {idx} added to the cart.")
    print("All products have been added to the cart.")
    logging.info("All products have been added to the cart.")


def remove_all_products_from_cart(driver):
    print("Removing all products from the cart...")
    logging.info("Removing all products from the cart.")
    items = driver.find_elements(By.CLASS_NAME, "btn_secondary")
    for idx, item in enumerate(items, start=1):
        item.click()
        print(f"Product {idx} removed from the cart.")
        logging.info(f"Product {idx} removed from the cart.")
    print("All products have been removed from the cart.")
    logging.info("All products have been removed from the cart.")


def run_tests():
    print("Executing the test suite...")
    logging.info("Executing the test suite...")


    print("Attempting to log in with 'standard_user'.")
    driver = login("standard_user", "secret_sauce")
    print("Login successful. Proceeding with the tests.")
    logging.info("Login successful with user 'standard_user'.")

    add_all_products_to_cart(driver)

    remove_all_products_from_cart(driver)

    driver.quit()
    print("Test suite execution completed. Browser closed.")
    logging.info("Test suite execution completed. Browser closed.")


if __name__ == "__main__":
    run_tests()
