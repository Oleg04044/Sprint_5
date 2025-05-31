import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.usefixtures("driver")
def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    wait = WebDriverWait(driver, 10)

    # Кнопка «Войти в аккаунт» на главной
    login_main_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))
    login_main_button.click()

    # Появились поля входа
    email_input = wait.until(EC.presence_of_element_located(EMAIL_INPUT))
    password_input = wait.until(EC.presence_of_element_located(PASSWORD_INPUT))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))

    # Вводим данные
    email_input.send_keys("oleg_bykhovskii_23@yandex.ru")
    password_input.send_keys("010595oleg")
    login_button.click()

    # Проверяем переход
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

@pytest.mark.usefixtures("driver")
def test_login_from_account_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    wait = WebDriverWait(driver, 10)

    # Кнопка «Личный кабинет»
    account_button = wait.until(EC.element_to_be_clickable(ACCOUNT_BUTTON))
    account_button.click()

    # Поля входа
    email_input = wait.until(EC.presence_of_element_located(EMAIL_INPUT))
    password_input = wait.until(EC.presence_of_element_located(PASSWORD_INPUT))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))

    # Вводим данные
    email_input.send_keys("oleg_bykhovskii_23@yandex.ru")
    password_input.send_keys("010595oleg")
    login_button.click()

    # Проверяем переход
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

@pytest.mark.usefixtures("driver")
def test_login_from_registration_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    wait = WebDriverWait(driver, 10)

    # Ссылка «Войти» на странице регистрации
    login_link = wait.until(EC.element_to_be_clickable(LOGIN_LINK))
    login_link.click()

    # Появились поля входа
    email_input = wait.until(EC.presence_of_element_located(EMAIL_INPUT))
    password_input = wait.until(EC.presence_of_element_located(PASSWORD_INPUT))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))

    # Вводим данные
    email_input.send_keys("oleg_bykhovskii_23@yandex.ru")
    password_input.send_keys("010595oleg")
    login_button.click()

    # Проверяем переход
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

@pytest.mark.usefixtures("driver")
def test_login_from_forgot_password_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    wait = WebDriverWait(driver, 10)

    # Ссылка «Войти» на странице восстановления пароля
    login_link = wait.until(EC.element_to_be_clickable(LOGIN_LINK))
    login_link.click()

    # Появились поля входа
    email_input = wait.until(EC.presence_of_element_located(EMAIL_INPUT))
    password_input = wait.until(EC.presence_of_element_located(PASSWORD_INPUT))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))

    # Вводим данные
    email_input.send_keys("oleg_bykhovskii_23@yandex.ru")
    password_input.send_keys("010595oleg")
    login_button.click()

    # Проверяем переход
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
