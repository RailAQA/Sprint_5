from locators import GeneralLocators, PersonalAccountLocator, OrderFeedLocators, LoginFormLocators
from tools.routes import AppRoute

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_navigate_from_order_feed_to_personal_account_with_state(driver_with_state):
    driver_with_state.get(AppRoute.ORDER_FEED)
    WebDriverWait(driver_with_state, 5).until(EC.visibility_of_element_located(OrderFeedLocators().ORDER_FEED_TITTLE))

    personal_account_button = driver_with_state.find_element(*GeneralLocators().PERSONAL_ACCOUNT_BUTTON)
    personal_account_button.click()
    WebDriverWait(driver_with_state, 5).until(EC.visibility_of_element_located(PersonalAccountLocator().SAVE_BUTTON))

    assert driver_with_state.current_url == AppRoute.PERSONAL_ACCOUNT

def test_navigate_from_order_feed_to_personal_account_without_state(driver):
    driver.get(AppRoute.ORDER_FEED)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(OrderFeedLocators().ORDER_FEED_TITTLE))

    personal_account_button = driver.find_element(*GeneralLocators().PERSONAL_ACCOUNT_BUTTON)
    personal_account_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    assert driver.current_url == AppRoute.LOGIN