from selenium.webdriver.common.by import By

# Страница входа
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле email
PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле пароль
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")  # Кнопка входа
LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")  # Ссылка «Войти» на страницах регистрации и восстановления пароля

# Страница регистрации
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле имя
REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле email (регистрация)
REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле пароль (регистрация)
REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # Кнопка регистрации
ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Сообщение об ошибке

# Личный кабинет
ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")  # Кнопка личного кабинета
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")  # Кнопка выхода

# Конструктор
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")  # Кнопка конструктора
STELLAR_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers

# Разделы конструктора
BUN_SECTION = (By.XPATH, "//span[text()='Булки']")  # Булки
SAUCE_SECTION = (By.XPATH, "//span[text()='Соусы']")  # Соусы
FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']")  # Начинки
