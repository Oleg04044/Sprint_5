import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.usefixtures("driver")
class TestConstructorSections:

    def test_sauce_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        wait = WebDriverWait(driver, 10)

        # Кликаем на «Соусы»
        sauce_section = wait.until(EC.element_to_be_clickable(SAUCE_SECTION))
        sauce_section.click()

        # Проверяем, что блок соусов активен
        active_tab = wait.until(EC.presence_of_element_located(ACTIVE_TAB_SAUCE))
        assert active_tab.text == "Соусы"

    def test_filling_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        wait = WebDriverWait(driver, 10)

        # Кликаем на «Начинки»
        filling_section = wait.until(EC.element_to_be_clickable(FILLING_SECTION))
        filling_section.click()

        # Проверяем, что блок начинок активен
        active_tab = wait.until(EC.presence_of_element_located(ACTIVE_TAB_FILLING))
        assert active_tab.text == "Начинки"

    def test_bun_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        wait = WebDriverWait(driver, 10)

        time.sleep(2)

        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal")))

        # Кликаем на «Булки»
        bun_section = wait.until(EC.element_to_be_clickable(BUN_SECTION))
        driver.execute_script("arguments[0].click();", bun_section)

        # Проверяем, что блок булок активен
        active_tab = wait.until(EC.presence_of_element_located(ACTIVE_TAB_BUN))
        assert active_tab.text == "Булки"
