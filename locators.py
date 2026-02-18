from selenium.webdriver.common.by import By

class GeneralLocators:
    HEADER = By.XPATH, '//header' # Шапка сайта
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//a[@href="/account"]' # Кнопка "Личный кабинет" в шапке
    CONSTRUCTOR_BUTTON =By.XPATH, '//a[@href="/"]' # Кнопка "Конструктор" в шапке
    LOGO_BUTTON = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]//a' # Логотип в шапке

class RegistrationFormLocators:
    NAME_INPUT = By.XPATH, '//label[text()="Имя"]/following::input[@class="text input__textfield text_type_main-default"]' # Поле "Имя" в форме регистрации
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following::input[@class="text input__textfield text_type_main-default"]' # Поле "Email" в форме регистрации
    PASSWORD_INPUT = By.XPATH, '//label[text()="Пароль"]/following::input[@class="text input__textfield text_type_main-default"]' # Поле "Пароль" в форме регистрации
    REGISTRATION_BUTTON = By.XPATH, '//button[text()="Зарегистрироваться"]' # Кнопка "Зарегистрироваться" в форме регистрации
    PASSWORD_ERROR_ALERT = By.XPATH, '//p[@class="input__error text_type_main-default"]' # Ошибка о некорректном пароле в форме регистрации
    LOGIN_BUTTON = By.XPATH, '//a[@href="/login"]' # Кнопка "Войти" в форме регистрации

class LoginFormLocators:
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following::input[@class="text input__textfield text_type_main-default"]' # Поле "Email" в форме авторизации
    PASSWORD_INPUT = By.XPATH, '//label[text()="Пароль"]/following::input[@class="text input__textfield text_type_main-default"]' # Поле "Пароль" в форме авторизации
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]' # Кнопка "Войти" в форме авторизации

class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]' # Кнопка "Войти в аккаунт" на главной странице
    PLACE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]' # Кнопка "Оформить заказ" на главной странице

    BREADS_BUTTON = By.XPATH, '//div[span[text()="Булки"]]' # Раздел "Булки" на главной странице
    SAUCES_BUTTON = By.XPATH, '//div[span[text()="Соусы"]]' # Раздел "Соусы" на главной странице
    TOPPINGS_BUTTON = By.XPATH, '//div[span[text()="Начинки"]]' # Раздел "Начинки" на главной странице

    BREADS_TITTLE = By.XPATH, '//h2[text()="Булки"]' # Заголовок раздела "Булки"  на главной странице
    SAUCES_TITTLE = By.XPATH, '//h2[text()="Соусы"]' # Заголовок раздела "Соусы"  на главной странице
    TOPPINGS_TITTLE = By.XPATH, '//h2[text()="Начинки"]' # Заголовок раздела "Начинки"  на главной странице
    
class PasswordRecoveryFormLocators:
    LOGIN_BUTTON = By.XPATH, '//a[@href="/login"]' # Кнопка "Войти" в форме восстановления пароля
    RECOVERY_BUTTON = By.XPATH, '//button[text()="Восстановить"]' # Кнопка "Восстановить" в форме восстановления пароля

class PersonalAccountLocator:
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]' # Кнопка "Сохранить" в личном кабинете
    LOGOUT_BUTTON = By.XPATH, '//button[text()="Выход"]' # Кнопка "Выход" в личном кабинете

class OrderFeedLocators:
    ORDER_FEED_TITTLE = By.XPATH, '//h1[text()="Лента заказов"]' # Заголовок страницы "Лента заказов"
