from tools.generator import generate_email, generate_valid_password
from locators import GeneralLocators, RegistrationFormLocators, LoginFormLocators, MainPageLocators, PasswordRecoveryFormLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_login_from_login_button(driver):
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

    driver.get("https://stellarburgers.education-services.ru")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(GeneralLocators().HEADER))

    login_main_page_button = driver.find_element(*MainPageLocators().LOGIN_ACCOUNT_BUTTON)
    login_main_page_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    email_authorization_form_input = driver.find_element(*LoginFormLocators().EMAIL_INPUT)
    email_authorization_form_input.send_keys(email)

    password_authorization_input = driver.find_element(*LoginFormLocators().PASSWORD_INPUT)
    password_authorization_input.send_keys(password)

    login_authorization_form_button = driver.find_element(*LoginFormLocators().LOGIN_BUTTON)
    login_authorization_form_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators().PLACE_ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"

def test_login_from_personal_account_button(driver):
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

    personal_account_button = driver.find_element(*GeneralLocators().PERSONAL_ACCOUNT_BUTTON)
    personal_account_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    email_authorization_form_input = driver.find_element(*LoginFormLocators().EMAIL_INPUT)
    email_authorization_form_input.send_keys(email)

    password_authorization_input = driver.find_element(*LoginFormLocators().PASSWORD_INPUT)
    password_authorization_input.send_keys(password)

    login_authorization_form_button = driver.find_element(*LoginFormLocators().LOGIN_BUTTON)
    login_authorization_form_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators().PLACE_ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"

def test_login_from_registration_form_login_button(driver):
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
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    driver.get("https://stellarburgers.education-services.ru/register")
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationFormLocators().REGISTRATION_BUTTON))

    login_registration_form_button = driver.find_element(*RegistrationFormLocators().LOGIN_BUTTON)
    login_registration_form_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    email_authorization_form_input = driver.find_element(*LoginFormLocators().EMAIL_INPUT)
    email_authorization_form_input.send_keys(email)

    password_authorization_input = driver.find_element(*LoginFormLocators().PASSWORD_INPUT)
    password_authorization_input.send_keys(password)

    login_authorization_form_button = driver.find_element(*LoginFormLocators().LOGIN_BUTTON)
    login_authorization_form_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators().PLACE_ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"

def test_login_from_recovery_password_form(driver):
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
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    driver.get("https://stellarburgers.education-services.ru/forgot-password")
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PasswordRecoveryFormLocators().RECOVERY_BUTTON))

    login_recovery_password_form = driver.find_element(*PasswordRecoveryFormLocators().LOGIN_BUTTON)
    login_recovery_password_form.click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(LoginFormLocators().LOGIN_BUTTON))

    email_authorization_form_input = driver.find_element(*LoginFormLocators().EMAIL_INPUT)
    email_authorization_form_input.send_keys(email)

    password_authorization_input = driver.find_element(*LoginFormLocators().PASSWORD_INPUT)
    password_authorization_input.send_keys(password)

    login_authorization_form_button = driver.find_element(*LoginFormLocators().LOGIN_BUTTON)
    login_authorization_form_button.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators().PLACE_ORDER_BUTTON))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"