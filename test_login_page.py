from .pages.login_page import LoginPage


def test_guest_see_login_page_forms(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_url()       # проверяем что присутсвует ссылка на страницу логина
    page.should_be_login_form()      # проверяем что присутсвует форма для логина
    page.should_be_register_form()   # проверяем что присутсвует форма для регистрации
