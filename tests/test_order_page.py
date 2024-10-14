import data
import allure
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage

class TestOrderPage:
    @allure.title('Проверяем создания заказа и перехода на главную страницу')
    @allure.description('Создание заказа с первым набором тестовых данных и с последущим перехом по логотипу Самоката')
    def test_up_order_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.set_order(
            data.NAME_1,
            data.SURNAME_1,
            data.ADDRESS_1,
            data.NUMBER_1,
            data.COMMENT_1
        )
        order_up_text = order_page.check_order(OrderPageLocators.ORDER_UP_LOCATOR)
        assert data.ORDER_UP in order_up_text
        order_page.click_to_element(OrderPageLocators.STATUS_ORDER_LOCATOR)
        order_page.click_to_element(OrderPageLocators.LOGO_SCOOTER_LOCATOR)
        assert order_page.check_url(data.HOME_URL_SCOOTER)

    @allure.title('Проверяем создания заказа и перехода на страницу dzen')
    @allure.description('Создание заказа с первым набором тестовых данных и с последущим перехом по логотипу Яндекса')
    def test_up_order_logo_yandex(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.set_order(
            data.NAME_2,
            data.SURNAME_2,
            data.ADDRESS_2,
            data.NUMBER_2,
            data.COMMENT_2
        )
        order_up_text = order_page.check_order(OrderPageLocators.ORDER_UP_LOCATOR)
        assert data.ORDER_UP in order_up_text
        order_page.click_to_element(OrderPageLocators.STATUS_ORDER_LOCATOR)
        order_page.click_to_element(OrderPageLocators.LOGO_YANDEX_LOCATOR)
        order_page.switch_to_new_window(data.URL_DZEN)
        assert order_page.check_url(data.URL_DZEN)

