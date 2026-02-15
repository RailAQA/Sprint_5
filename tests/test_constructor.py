from locators import GeneralLocators, PersonalAccountLocator, LoginFormLocators, MainPageLocators

from selenium.webdriver.support import expected_conditions as EC
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

def test_navigate_to_sauces_section(driver):
    driver.get("https://stellarburgers.education-services.ru")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(GeneralLocators().HEADER))

    sauces_button = driver.find_element(*MainPageLocators().SAUCES_BUTTON)
    sauces_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators().SAUCES_TITTLE))

    assert "tab_tab_type_current__2BEPc pt-4" in sauces_button.get_attribute("class")

def test_default_state_for_breads_button(driver):
    driver.get("https://stellarburgers.education-services.ru")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(GeneralLocators().HEADER))

    breads_button = driver.find_element(*MainPageLocators.BREADS_BUTTON)
    assert "tab_tab_type_current__2BEPc pt-4" in breads_button.get_attribute("class")

def test_navigate_to_toppings_section(driver):
    driver.get("https://stellarburgers.education-services.ru")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(GeneralLocators().HEADER))

    toppings_button = driver.find_element(*MainPageLocators().TOPPINGS_BUTTON)
    toppings_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators().TOPPINGS_TITTLE))

    assert "tab_tab_type_current__2BEPc pt-4" in toppings_button.get_attribute("class")

def test_navigate_to_breads_section(driver):
    driver.get("https://stellarburgers.education-services.ru")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(GeneralLocators().HEADER))

    sauces_button = driver.find_element(*MainPageLocators().SAUCES_BUTTON)
    sauces_button.click()

    breads_button = driver.find_element(*MainPageLocators.BREADS_BUTTON)
    breads_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators().BREADS_TITTLE))

    assert "tab_tab_type_current__2BEPc pt-4" in breads_button.get_attribute("class")
