import datetime

import pytest

from restaurant.tests.common_fixtures.reset_sequence import reset


class TestTableNotFoundResponse:
    @pytest.fixture
    def presenter(self):
        from restaurant.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_table_not_found_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'TABLE_NOT_FOUND',
            'response': 'Table not found: f32b2f96-93f5-4e2f-842d-d590783dc001',
            'status_code': 400
        }

        # Act
        response = presenter.table_not_found_response(table_id='f32b2f96-93f5-4e2f-842d-d590783dc001')

        # Arrange
        assert response == expected_response
