import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.usefixtures("driver")
def test_go_to_account_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")

    wait = WebDriverWait(driver, 10)

    # Ввод логина и пароля
    email_input = wait.until(EC.presence_of_element_located(EMAIL_INPUT))
    password_input = wait.until(EC.presence_of_element_located(PASSWORD_INPUT))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))

    email_input.send_keys("oleg_bykhovskii_23@yandex.ru")
    password_input.send_keys("010595oleg")
    login_button.click()

    # Переход в Личный кабинет
    account_button = wait.until(EC.element_to_be_clickable(ACCOUNT_BUTTON))
    account_button.click()

    # Проверяем, что открыта страница профиля
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

@pytest.mark.usefixtures("driver")
def test_go_to_constructor_from_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")

    wait = WebDriverWait(driver, 10)

    # Ввод логина и пароля
    email_input = wait.until(EC.presence_of_element_located(EMAIL_INPUT))
    password_input = wait.until(EC.presence_of_element_located(PASSWORD_INPUT))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))

    email_input.send_keys("oleg_bykhovskii_23@yandex.ru")
    password_input.send_keys("010595oleg")
    login_button.click()

    # Переходим в Личный кабинет
    account_button = wait.until(EC.element_to_be_clickable(ACCOUNT_BUTTON))
    account_button.click()

    # Кликаем по «Конструктор»
    constructor_button = wait.until(EC.element_to_be_clickable(CONSTRUCTOR_BUTTON))
    constructor_button.click()

    # Проверяем, что вернулись на главную
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    # Снова заходим в Личный кабинет
    account_button = wait.until(EC.element_to_be_clickable(ACCOUNT_BUTTON))
    account_button.click()

    # Кликаем по логотипу Stellar Burgers
    logo = wait.until(EC.element_to_be_clickable(STELLAR_LOGO))
    logo.click()

    # Проверяем, что снова вернулись на главную
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

@pytest.mark.usefixtures("driver")
def test_logout_from_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")

    wait = WebDriverWait(driver, 10)

    # Ввод логина и пароля
    email_input = wait.until(EC.presence_of_element_located(EMAIL_INPUT))
    password_input = wait.until(EC.presence_of_element_located(PASSWORD_INPUT))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))

    email_input.send_keys("oleg_bykhovskii_23@yandex.ru")
    password_input.send_keys("010595oleg")
    login_button.click()

    # Переходим в Личный кабинет
    account_button = wait.until(EC.element_to_be_clickable(ACCOUNT_BUTTON))
    account_button.click()

    # Кликаем по кнопке «Выход»
    logout_button = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
    logout_button.click()

    # Проверяем, что перешли на страницу входа
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
