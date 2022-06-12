import datetime

import pytest

from restaurant.tests.common_fixtures.reset_sequence import reset


class TestItemsNotFoundResponse:
    @pytest.fixture
    def presenter(self):
        from restaurant.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_items_not_found(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'SELECTED_ITEMS_NOT_FOUND',
            'response': "Items not found: ['f32b2f96-93f5-4e2f-842d-d590783dc001']",
            'status_code': 400
        }

        # Act
        response = presenter.items_not_found(item_ids=['f32b2f96-93f5-4e2f-842d-d590783dc001'])

        # Arrange
        assert response == expected_response
