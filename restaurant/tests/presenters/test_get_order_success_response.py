import pytest

from restaurant.tests.common_fixtures.factories import OrderDTOFactory, UserDetailsDTOFactory, ItemDTOFactory
from restaurant.tests.common_fixtures.reset_sequence import reset


class TestGetOrderResponse:
    @pytest.fixture
    def presenter(self):
        from restaurant.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_get_order_response(self, presenter):
        # Arrange
        reset()
        user_dto = UserDetailsDTOFactory(username="kamala", first_name="Kamala")
        order_dto = OrderDTOFactory()
        item_dtos = ItemDTOFactory.create_batch(size=4)
        expected_response = self._get_expected_response()

        # Act
        response = presenter.get_order_response(
            user_dto=user_dto, order_dto=order_dto, item_dtos=item_dtos
        )

        # Arrange
        assert response == expected_response

    def _get_expected_response(self):
        return {
            "first_name":"Kamala",
            "order":{
                "amount":0,
                "id":"d32b2f96-93f5-4e2f-842d-d590783dc000",
                "is_paid":True,
                "items":[
                    {
                        "description":"",
                        "id":"d32b2f96-93f5-4e2f-842d-d590783dc000",
                        "name":"Item 0",
                        "price":3000
                    },
                    {
                        "description":"",
                        "id":"d32b2f96-93f5-4e2f-842d-d590783dc001",
                        "name":"Item 1",
                        "price":3000
                    },
                    {
                        "description":"",
                        "id":"d32b2f96-93f5-4e2f-842d-d590783dc002",
                        "name":"Item 2",
                        "price":3000
                    },
                    {
                        "description":"",
                        "id":"d32b2f96-93f5-4e2f-842d-d590783dc003",
                        "name":"Item 3",
                        "price":3000
                    }
                ]
            },
            "user_id":"d32b2f96-93f5-4e2f-842d-d590783dc000",
            "username":"kamala"
        }
