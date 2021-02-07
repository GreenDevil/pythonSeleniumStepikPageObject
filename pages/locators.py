from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_link")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME_H1 = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_SUCCESS = (By.CLASS_NAME, "alertinner")
    MAIN_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET = (By.CLASS_NAME, "basket-mini")