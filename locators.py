from selenium.webdriver.common.by import By

class GeneralLocators:
    HEADER = By.XPATH, '//header'
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//a[@href="/account"]'
    CONSTRUCTOR_BUTTON =By.XPATH, '//a[@href="/"]'
    LOGO_BUTTON = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]//a'

class RegistrationFormLocators:
    NAME_INPUT = By.XPATH, '//label[text()="Имя"]/following::input[@class="text input__textfield text_type_main-default"]'
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following::input[@class="text input__textfield text_type_main-default"]'
    PASSWORD_INPUT = By.XPATH, '//label[text()="Пароль"]/following::input[@class="text input__textfield text_type_main-default"]'
    REGISTRATION_BUTTON = By.XPATH, '//button[text()="Зарегистрироваться"]'
    PASSWORD_ERROR_ALERT = By.XPATH, '//p[@class="input__error text_type_main-default"]'
    LOGIN_BUTTON = By.XPATH, '//a[@href="/login"]'

class LoginFormLocators:
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following::input[@class="text input__textfield text_type_main-default"]'
    PASSWORD_INPUT = By.XPATH, '//label[text()="Пароль"]/following::input[@class="text input__textfield text_type_main-default"]'
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'

class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'
    PLACE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    
class PasswordRecoveryFormLocators:
    LOGIN_BUTTON = By.XPATH, '//a[@href="/login"]'
    RECOVERY_BUTTON = By.XPATH, '//button[text()="Восстановить"]'

class PersonalAccountLocator:
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'

class OrderFeedLocators:
    ORDER_FEED_TITTLE = By.XPATH, '//h1[text()="Лента заказов"]'