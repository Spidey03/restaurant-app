import datetime

import pytest

from restaurant.tests.common_fixtures.reset_sequence import reset


class TestItemsNotSelected:
    @pytest.fixture
    def presenter(self):
        from restaurant.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_no_items_selected_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'NO_ITEMS_SELECTED',
            'response': 'Please select atleast one item',
            'status_code': 400
        }

        # Act
        response = presenter.no_items_selected_response()

        # Arrange
        assert response == expected_response
