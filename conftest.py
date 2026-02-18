from locators import GeneralLocators, RegistrationFormLocators, LoginFormLocators, MainPageLocators
from tools.generator import generate_email, generate_valid_password
from tools.selenium.drivers import initialize_driver
from tools.browsers import AppBrowsers
from tools.routes import AppRoute

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest


email = generate_email()
password = generate_valid_password()

@pytest.fixture
def driver():
    yield from initialize_driver(browser=AppBrowsers.CHROMIUM)

@pytest.fixture
def driver_create_state(driver):    
    driver.get(AppRoute.REGISTRATION)
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
    yield driver

@pytest.fixture
def driver_with_state(driver):
    driver.get(AppRoute.LOGIN)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    email_authorization_form_input = driver.find_element(*LoginFormLocators().EMAIL_INPUT)
    email_authorization_form_input.send_keys("qwerty123@mail.ru")

    password_authorization_input = driver.find_element(*LoginFormLocators().PASSWORD_INPUT)
    password_authorization_input.send_keys("Railka123")

    login_authorization_form_button = driver.find_element(*LoginFormLocators().LOGIN_BUTTON)
    login_authorization_form_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators().PLACE_ORDER_BUTTON))
    yield driver