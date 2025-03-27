from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")

    def test_login(self):
        driver = self.driver
        
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

        self.assertIn("Swag Labs", driver.title)

    def test_add_to_cart(self):
        driver = self.driver
        
        self.test_login()  
        add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()

        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

        self.assertEqual(cart_badge.text, "1")

    def test_remove_from_cart(self):
        driver = self.driver
        
        self.test_add_to_cart()
        remove_button = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        remove_button.click()

        cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

        self.assertEqual(len(cart_badge), 0)

    def test_product_details(self):
        driver = self.driver
        
        self.test_login()
        product_link = driver.find_element(By.ID, "item_4_title_link")
        product_link.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_name")))

        product_name = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
        self.assertEqual(product_name, "Sauce Labs Backpack")

    def test_navigation_to_cart(self):
        driver = self.driver
        
        self.test_login()
        cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))

        self.assertIn("Your Cart", driver.find_element(By.CLASS_NAME, "title").text)

    def test_error_message_for_locked_user(self):
        driver = self.driver
        
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        login_button.click()

        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Sorry, this user has been locked out.", error_message)

    def test_check_product_prices(self):
        driver = self.driver
        
        self.test_login()
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        
        self.assertTrue(len(prices) > 0)
        for price in prices:
            self.assertRegex(price.text, r'^\$\d+\.\d{2}$')

    def test_add_multiple_products_to_cart(self):
        driver = self.driver
        
        self.test_login()
        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(@id, 'add-to-cart')]")
        
        for button in add_to_cart_buttons[:3]:
            button.click()

        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, "3")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
