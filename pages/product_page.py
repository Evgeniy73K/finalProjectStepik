import math

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_success_alert(self):
        product_name_in_alert_name = self.browser.find_element(By.XPATH, "//div[@class=\"alert alert-safe alert-noicon alert-success  fade in\"]//strong")
        product_name = self.browser.find_element(By.XPATH, "//div[@class=\"col-sm-6 product_main\"]/h1")
        assert product_name_in_alert_name.text == product_name.text, "names are not equals"
        i = 0

    def should_be_product_price_equals_cart_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        assert product_price.text in cart_price.text, "product price and cart price are not equals"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
