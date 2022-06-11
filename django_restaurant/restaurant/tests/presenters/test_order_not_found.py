import datetime

import pytest

from restaurant.tests.common_fixtures.reset_sequence import reset


class TestOrderNotFound:
    @pytest.fixture
    def presenter(self):
        from restaurant.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_order_not_found(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'ORDER_NOT_FOUND',
            'response': "Order not exist, d32b2f96-93f5-4e2f-842d-d590783dc000",
            'status_code': 400
        }

        # Act
        response = presenter.order_not_found(order_id="d32b2f96-93f5-4e2f-842d-d590783dc000")

        # Arrange
        assert response == expected_response
