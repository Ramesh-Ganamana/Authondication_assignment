from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Selection:
    input_bar = "///input[@id='twotabsearchtextbox']"
    search_button = "//input[@id='nav-search-submit-button']"
    wrist_type = "//span[text()='Wrist']"
    selecting_any_watch = "(//div[@data-component-type='s-search-result'])[1]"
    add_to_cart = "//span[@id='submit.add-to-cart']"
    skip_button = "(//span[text()=' Skip '])[1]"
    cart_icon = "//a[@id='nav-cart']"
    proceed_to_buy = "//input[@name='proceedToRetailCheckout']"

    def __init__(self, driver):
        self.driver = driver

    def selecting_items(self):
        self.driver.find_element(By.XPATH, self.input_bar).click()
        self.driver.find_element(By.XPATH, self.input_bar).send_keys("Watches for men")
        self.driver.find_element(By.XPATH, self.search_button).click()
        time.sleep(10)

    def switching_window(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.wrist_type).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.selecting_any_watch).click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)

    def item_added_to_cart(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.add_to_cart).click()
        time.sleep(10)

    def proceed_to_payment(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.cart_icon).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.proceed_to_buy).click()
        time.sleep(10)
    "After clicking on this website, it prompts for a login. As I'm unable to provide personal information here, I am concluding this session."