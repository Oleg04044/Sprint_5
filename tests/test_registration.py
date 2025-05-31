import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data_generator import generate_email

@pytest.mark.usefixtures("driver")
def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    wait = WebDriverWait(driver, 10)

    # Явные ожидания появления полей
    name_input = wait.until(EC.presence_of_element_located(NAME_INPUT))
    email_input = wait.until(EC.presence_of_element_located(REGISTER_EMAIL_INPUT))
    password_input = wait.until(EC.presence_of_element_located(REGISTER_PASSWORD_INPUT))
    register_button = wait.until(EC.element_to_be_clickable(REGISTER_BUTTON))

    # Используем генератор email
    email = generate_email()

    # Вводим данные
    name_input.send_keys("Олег")
    email_input.send_keys(email)
    password_input.send_keys("010595oleg")
    register_button.click()

    # Проверяем, что после регистрации переходим на страницу логина
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

@pytest.mark.usefixtures("driver")
def test_registration_with_short_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    wait = WebDriverWait(driver, 10)

    name_input = wait.until(EC.presence_of_element_located(NAME_INPUT))
    email_input = wait.until(EC.presence_of_element_located(REGISTER_EMAIL_INPUT))
    password_input = wait.until(EC.presence_of_element_located(REGISTER_PASSWORD_INPUT))
    register_button = wait.until(EC.element_to_be_clickable(REGISTER_BUTTON))

    email = generate_email()

    # Вводим данные с коротким паролем
    name_input.send_keys("Олег")
    email_input.send_keys(email)
    password_input.send_keys("123")  # Слишком короткий пароль
    register_button.click()

    # Проверяем, что появилось сообщение об ошибке
    error_message = wait.until(EC.presence_of_element_located(ERROR_MESSAGE))
    assert error_message.text == "Некорректный пароль"
