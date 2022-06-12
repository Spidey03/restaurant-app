import datetime

import pytest

from restaurant.tests.common_fixtures.reset_sequence import reset


class TestOrderCreatedSuccessfuls:
    @pytest.fixture
    def presenter(self):
        from restaurant.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_login_successful_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'ORDER_CREATE_SUCCESSFULLY',
            'response': "We've recieved order, please be patient we'll serve to you soon, "
             'order_id: f32b2f96-93f5-4e2f-842d-d590783dc001',
            'status_code': 201
        }

        # Act
        response = presenter.order_created_successfully(order_id='f32b2f96-93f5-4e2f-842d-d590783dc001')

        # Arrange
        assert response == expected_response
