from locators import GeneralLocators, PersonalAccountLocator, OrderFeedLocators, LoginFormLocators

from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.ui import WebDriverWait


def test_navigate_from_constructor_to_personal_account_with_state(driver_with_state):
    personal_account_button = driver_with_state.find_element(*GeneralLocators().PERSONAL_ACCOUNT_BUTTON)
    personal_account_button.click()
    WebDriverWait(driver_with_state, 5).until(EC.visibility_of_element_located(PersonalAccountLocator().SAVE_BUTTON))

    assert driver_with_state.current_url == "https://stellarburgers.education-services.ru/account/profile"

def test_navigate_from_constructor_to_personal_account_without_state(driver):
    driver.get("https://stellarburgers.education-services.ru")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(GeneralLocators().HEADER))

    personal_account_button = driver.find_element(*GeneralLocators().PERSONAL_ACCOUNT_BUTTON)
    personal_account_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/login"
