from tools.generator import generate_email, generate_valid_password
from locators import GeneralLocators, RegistrationFormLocators, LoginFormLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_successful_registration(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
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

    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

