import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.usefixtures("driver")
def test_constructor_sections(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    wait = WebDriverWait(driver, 10)

    # Кликаем на «Соусы»
    sauce_section = wait.until(EC.element_to_be_clickable(SAUCE_SECTION))
    sauce_section.click()


    active_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span[text()='Соусы']")))
    assert active_tab.text == "Соусы"

    # Кликаем на «Начинки»
    filling_section = wait.until(EC.element_to_be_clickable(FILLING_SECTION))
    filling_section.click()

    active_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span[text()='Начинки']")))
    assert active_tab.text == "Начинки"

    # Кликаем на «Булки»
    bun_section = wait.until(EC.element_to_be_clickable(BUN_SECTION))
    bun_section.click()

    active_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span[text()='Булки']")))
    assert active_tab.text == "Булки"
