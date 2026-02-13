from selenium.webdriver.common.by import By


NAME_REGISTRATION_FORM_INPUT = By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@class="text input__textfield text_type_main-default"]'
EMAIL_REGISTRATION_FORM_INPUT = By.NAME, '//div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]//input[@class="text input__textfield text_type_main-default"]'
PASSWORD_REGISTRATION_FORM_INPUT = By.NAME, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@class="text input__textfield text_type_main-default"]'