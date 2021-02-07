import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
    # url адрес
    page.open()                             # открываем страницу
    page.go_to_login_page()                 # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()       # выполняем метод страницы — выполняем поиск ссылки на логин


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.should_be_login_link()     # выполняем метод страницы — выполняем поиск ссылки на логин


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # Данная часть не реализована в тестовом магазине, но можно использовать для предусловия и постусловия в тестах
    # @pytest.fixture(scope="function", autouse=True)
    # def setup(self):
    #     self.product = ProductFactory(title="Best book created by robot")
    #     # создаем по апи
    #     self.link = self.product.link
    #     yield
    #     # после этого ключевого слова начинается teardown
    #     # выполнится после каждого теста в классе
    #     # удаляем те данные, которые мы создали
    #     self.product.delete()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        # адрес
        page.open()                     # открываем страницу
        page.go_to_basket()             # переходим по кнопке в корзину
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_products_in_basket()  # Ожидаем, что в корзине нет товаров
        basket_page.should_basket_empty_text_present()  # Ожидаем, что есть текст о том что корзина пуста

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        # адрес
        page.open()                     # открываем страницу
        page.go_to_basket()             # переходим по кнопке в корзину
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_products_in_basket()  # Ожидаем, что в корзине нет товаров
        basket_page.should_basket_empty_text_present()  # Ожидаем, что есть текст о том что корзина пуста

