import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
    # url адрес
    page.open()                                # открываем страницу
    page.should_be_add_to_basket_button()      # проверяем что присутсвует кнопка для добавления в корзину
    product_name = page.save_product_name()    # сохраняем наименование продукта
    product_value = page.save_product_value()  # сохраняем цену продукта
    page.add_to_basket()                       # добавляем товар в корзину
    page.solve_quiz_and_get_code()             # решаем задачку
    page.should_be_product_in_basket_message(product_name)     # проверяем что присутствует сообщение о том что
    # нужный товар добавлен в корзину
    page.should_be_basket_value(product_value)      # проверяем стоимость товаров в корзине


@pytest.mark.tasks
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
    # url адрес
    page.open()                            # открываем страницу
    page.should_be_add_to_basket_button()  # проверяем что присутсвует кнопка для добавления в корзину
    page.add_to_basket()                   # добавляем товар в корзину
    page.should_not_be_success_message()   # проверяем что нет сообщения о добавлении товара в корзину


@pytest.mark.tasks
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
    # url адрес
    page.open()                           # открываем страницу
    page.should_not_be_success_message()  # проверяем что нет сообщения о добавлении товара в корзину


@pytest.mark.tasks
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
    # url адрес
    page.open()                                 # открываем страницу
    page.should_be_add_to_basket_button()       # проверяем что присутсвует кнопка для добавления в корзину
    page.add_to_basket()                        # добавляем товар в корзину
    page.should_success_message_disappeared()   # проверяем что сообщения о добавлении товара в корзину исчезло
