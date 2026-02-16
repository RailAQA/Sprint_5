from tools.generator import generate_email, generate_valid_password, generate_wrong_password_with_1_symbol, generate_wrong_password_with_4_symbols, generate_wrong_password_with_5_symbols
from tools.routes import AppRoute
from locators import GeneralLocators, RegistrationFormLocators, LoginFormLocators

from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.ui import WebDriverWait


def test_successful_registration(driver):
    driver.get(AppRoute.REGISTRATION)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(GeneralLocators().HEADER))

    name_input = driver.find_element(*RegistrationFormLocators().NAME_INPUT)
    name_input.send_keys('Antonio')

    email_input = driver.find_element(*RegistrationFormLocators().EMAIL_INPUT)
    random_email = generate_email()
    email_input.send_keys(random_email)

    password_input = driver.find_element(*RegistrationFormLocators().PASSWORD_INPUT)
    random_valid_password = generate_valid_password()
    password_input.send_keys(random_valid_password)

    registration_button = driver.find_element(*RegistrationFormLocators().REGISTRATION_BUTTON)
    registration_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    assert driver.current_url == AppRoute.LOGIN

@pytest.mark.parametrize(
        "wrong_password", 
        (
              generate_wrong_password_with_1_symbol(),
                generate_wrong_password_with_4_symbols(),
                  generate_wrong_password_with_5_symbols()
                  ))
def test_with_wrong_password(driver, wrong_password):
    driver.get(AppRoute.REGISTRATION)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(GeneralLocators().HEADER))

    name_input = driver.find_element(*RegistrationFormLocators().NAME_INPUT)
    name_input.send_keys('Antonio')

    email_input = driver.find_element(*RegistrationFormLocators().EMAIL_INPUT)
    random_email = generate_email()
    email_input.send_keys(random_email)

    password_input = driver.find_element(*RegistrationFormLocators().PASSWORD_INPUT)
    password_input.send_keys(wrong_password)

    registration_button = driver.find_element(*RegistrationFormLocators().REGISTRATION_BUTTON)
    registration_button.click()

    error_alert = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationFormLocators().PASSWORD_ERROR_ALERT))
    assert error_alert.is_displayed()
    assert error_alert.text == "Некорректный пароль"
