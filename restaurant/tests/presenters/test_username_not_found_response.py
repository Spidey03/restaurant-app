import pytest

from restaurant.tests.common_fixtures.reset_sequence import reset


class TestUsernameNotFoundResponse:
    @pytest.fixture
    def presenter(self):
        from restaurant.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_username_not_found_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'USERNAME_NOT_FOUND',
            'response': 'Entered username not found: joey567',
            'status_code': 400,
        }

        # Act
        response = presenter.username_not_found_response(username='joey567')

        # Arrange
        assert response == expected_response
