from selenium.webdriver.common.by import By
class OrderPageLocators:

    ORDER_BUTTON_LOCATOR = By.XPATH, "//button[text()='Заказать']"
    NAME_LOCATOR = By.XPATH, "//input[@placeholder='* Имя']"
    SURNAME_LOCATOR = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_LOCATOR = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    STATION_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']"
    STATION_ROKOSOVSKY_LOCATOR = By.XPATH, '//div[@class="Order_Text__2broi" and text()="Бульвар Рокоссовского"]'
    NUMBER_LOCATOR = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON_LOCATOR = By.XPATH, "//button[text()='Далее']"
    DATA_LOCATOR = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    CALENDAR_LOCATOR = By.XPATH, '//div[@aria-label="Choose суббота, 19-е октября 2024 г."]'
    RENTAL_PERIOD_LOCATOR = By.XPATH, '//div[@class="Dropdown-placeholder" and text()="* Срок аренды"]'
    PERIOD_LOCATOR = By.XPATH, '//div[@role="option" and text()="сутки"]'
    COLOR_LOCATOR = By.ID, 'black'
    COMMENT_LOCATOR = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    ORDER_LOCATOR = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'
    YES_LOCATOR = By.XPATH, '//button[text()="Да"]'
    ORDER_UP_LOCATOR = By.XPATH, '//*[@class="Order_ModalHeader__3FDaJ"]'
    STATUS_ORDER_LOCATOR = By.CSS_SELECTOR, '.Order_NextButton__1_rCA > button:nth-child(1)'
    LOGO_SCOOTER_LOCATOR = By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR > img:nth-child(1)'
    LOGO_YANDEX_LOCATOR = By.XPATH, '//img[@alt="Yandex"]'


