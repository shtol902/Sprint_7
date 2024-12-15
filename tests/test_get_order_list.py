import allure


@allure.suite("Тесты на получение списка заказов")
class TestGetOrders:

    @allure.title("Получение списка всех заказов")
    def test_get_orders_without_courier_id(self, order_methods):
        status_code, response = order_methods.get_orders()

        assert status_code == 200
        assert "availableStations" in response
        assert isinstance(response["availableStations"], list)