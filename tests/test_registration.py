import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from urls import BASE_URL


@pytest.mark.usefixtures("driver")
class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(BASE_URL + "/register")
        wait = WebDriverWait(driver, 10)

        # Генерируем уникальный email для каждого запуска теста
        unique_email = f"test_{int(time.time())}@yopmail.com"

        name_input = wait.until(EC.presence_of_element_located(NAME_INPUT))
        email_input = wait.until(EC.presence_of_element_located(REGISTER_EMAIL_INPUT))
        password_input = wait.until(EC.presence_of_element_located(REGISTER_PASSWORD_INPUT))
        register_button = wait.until(EC.element_to_be_clickable(REGISTER_BUTTON))

        # Вводим данные
        name_input.send_keys("Test User")
        email_input.send_keys(unique_email)
        password_input.send_keys("010595oleg")
        register_button.click()

        # Проверяем, что после регистрации происходит переход на страницу логина
        wait.until(EC.url_to_be(BASE_URL + "/login"))
        assert driver.current_url == BASE_URL + "/login"

    def test_registration_with_short_password(self, driver):
        driver.get(BASE_URL + "/register")
        wait = WebDriverWait(driver, 10)

        name_input = wait.until(EC.presence_of_element_located(NAME_INPUT))
        email_input = wait.until(EC.presence_of_element_located(REGISTER_EMAIL_INPUT))
        password_input = wait.until(EC.presence_of_element_located(REGISTER_PASSWORD_INPUT))
        register_button = wait.until(EC.element_to_be_clickable(REGISTER_BUTTON))

        # Вводим некорректный (короткий) пароль
        name_input.send_keys("Test User")
        email_input.send_keys("oleg_bykhovskii_23@yandex.ru")
        password_input.send_keys("123")
        register_button.click()

        # Проверяем, что появляется сообщение об ошибке
        error_message = wait.until(EC.presence_of_element_located(ERROR_MESSAGE))
        assert error_message.is_displayed()
