from pages.base_page import BasePage
import allure
import data
from locators.order_page_locators import OrderPageLocators
class OrderPage(BasePage):

    @allure.step('Открытие страницы заказа')
    def open_order_page(self):
        self.driver.get(data.HOME_URL_SCOOTER)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_LOCATOR)

    @allure.step('Создание заказ')
    def set_order(self, name, surname, address, number, comment):
        self.add_text_to_element(OrderPageLocators.NAME_LOCATOR, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_LOCATOR, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_LOCATOR, address)
        self.click_to_element(OrderPageLocators.STATION_LOCATOR)
        self.click_to_element(OrderPageLocators.STATION_ROKOSOVSKY_LOCATOR)
        self.add_text_to_element(OrderPageLocators.NUMBER_LOCATOR, number)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON_LOCATOR)
        self.click_to_element(OrderPageLocators.DATA_LOCATOR)
        self.click_to_element(OrderPageLocators.CALENDAR_LOCATOR)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.COLOR_LOCATOR)
        self.add_text_to_element(OrderPageLocators.COMMENT_LOCATOR, comment)
        self.click_to_element(OrderPageLocators.ORDER_LOCATOR)
        self.click_to_element(OrderPageLocators.YES_LOCATOR)

    @allure.step('Проверка на создание заказа')
    def check_order(self, locator):
        return self.get_text_from_element(locator)

    @allure.step('Проверка перехода по URL')
    def check_url(self, url):
        return self.driver.current_url == url