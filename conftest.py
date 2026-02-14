from tools.generator import generate_email, generate_valid_password
from locators import GeneralLocators, RegistrationFormLocators, LoginFormLocators, MainPageLocators

from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def driver_with_state():
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.education-services.ru/register")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(GeneralLocators().HEADER))

    name_input = driver.find_element(*RegistrationFormLocators().NAME_INPUT)
    name_input.send_keys('Antonio')

    email_input = driver.find_element(*RegistrationFormLocators().EMAIL_INPUT)
    email = generate_email()
    email_input.send_keys(email)

    password_input = driver.find_element(*RegistrationFormLocators().PASSWORD_INPUT)
    password = generate_valid_password()
    password_input.send_keys(password)

    registration_button = driver.find_element(*RegistrationFormLocators().REGISTRATION_BUTTON)
    registration_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    email_authorization_form_input = driver.find_element(*LoginFormLocators().EMAIL_INPUT)
    email_authorization_form_input.send_keys(email)

    password_authorization_input = driver.find_element(*LoginFormLocators().PASSWORD_INPUT)
    password_authorization_input.send_keys(password)

    login_authorization_form_button = driver.find_element(*LoginFormLocators().LOGIN_BUTTON)
    login_authorization_form_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators().PLACE_ORDER_BUTTON))

    yield driver
    driver.quit()