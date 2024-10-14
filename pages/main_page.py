from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    @allure.step('Получение текста с ответа на вопрос {num}')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(
            MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(
            MainPageLocators.ANSWER_LOCATOR, num)

        self.click_to_element(MainPageLocators.CONFIRM_BUTTON_LOCATOR)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_8)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator_q_formatted)
        )
        self.click_to_element(locator_q_formatted)

        # Ожидание видимости элемента ответа
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator_a_formatted)
        )

        return self.get_text_from_element(locator_a_formatted)

