from locators import GeneralLocators, PersonalAccountLocator, MainPageLocators, LoginFormLocators
from tools.routes import AppRoute

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_navigate_from_personal_account_to_constructor(driver_with_state):
    personal_account_button = driver_with_state.find_element(*GeneralLocators.PERSONAL_ACCOUNT_BUTTON)
    personal_account_button.click()
    WebDriverWait(driver_with_state, 5).until(EC.visibility_of_element_located(PersonalAccountLocator().SAVE_BUTTON))

    constructor_button = driver_with_state.find_element(*GeneralLocators.CONSTRUCTOR_BUTTON)
    constructor_button.click()
    WebDriverWait(driver_with_state, 5).until(EC.visibility_of_element_located(MainPageLocators().PLACE_ORDER_BUTTON))

    assert driver_with_state.current_url == "https://stellarburgers.education-services.ru/"

def test_navigate_from_personal_account_to_constructor_from_logo(driver_with_state):
    personal_account_button = driver_with_state.find_element(*GeneralLocators.PERSONAL_ACCOUNT_BUTTON)
    personal_account_button.click()
    WebDriverWait(driver_with_state, 5).until(EC.visibility_of_element_located(PersonalAccountLocator().SAVE_BUTTON))

    logo_button = driver_with_state.find_element(*GeneralLocators.LOGO_BUTTON)
    logo_button.click()
    WebDriverWait(driver_with_state, 5).until(EC.visibility_of_element_located(MainPageLocators().PLACE_ORDER_BUTTON))

    assert driver_with_state.current_url == "https://stellarburgers.education-services.ru/"

def test_logout_from_personal_account(driver_with_state):
    personal_account_button = driver_with_state.find_element(*GeneralLocators.PERSONAL_ACCOUNT_BUTTON)
    personal_account_button.click()
    WebDriverWait(driver_with_state, 5).until(EC.visibility_of_element_located(PersonalAccountLocator().SAVE_BUTTON))

    logout_button = driver_with_state.find_element(*PersonalAccountLocator().LOGOUT_BUTTON)
    logout_button.click()
    WebDriverWait(driver_with_state, 5).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    assert driver_with_state.current_url == AppRoute.LOGIN
