from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Поиск элементов
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Клик по элементу
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    # Ввод текста
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # Получение текста элемента
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # Скролл
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Форматирование локаторов
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator


    def switch_to_new_window(self, url):
        current_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != current_window:
                self.driver.switch_to.window(window_handle)
                break
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))