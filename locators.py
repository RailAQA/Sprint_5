from selenium.webdriver.common.by import By

class GeneralLocators:
    HEADER = By.XPATH, '//header'

class RegistrationFormLocators:
    NAME_INPUT = By.XPATH, '//label[text()="Имя"]/following::input[@class="text input__textfield text_type_main-default"]'
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following::input[@class="text input__textfield text_type_main-default"]'
    PASSWORD_INPUT = By.XPATH, '//label[text()="Пароль"]/following::input[@class="text input__textfield text_type_main-default"]'
    REGISTRATION_BUTTON = By.XPATH, '//button[text()="Зарегистрироваться"]'

class LoginFormLocators:
    EMAIL_INPUT = By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input'
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'
    PASSWORD_ERROR_ALERT = By.XPATH, '//p[@class="input__error text_type_main-default"]'