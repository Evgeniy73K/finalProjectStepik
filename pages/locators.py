from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_PRICE = (By.XPATH, "//p[@class=\"price_color\"]")
    CART_PRICE = (By.CSS_SELECTOR, ".basket-mini")
