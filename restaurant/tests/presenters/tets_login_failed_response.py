import pytest

from restaurant.tests.common_fixtures.reset_sequence import reset


class TestLoginFailedResponse:
    @pytest.fixture
    def presenter(self):
        from restaurant.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_login_failed_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'LOGIN_FAILED',
            'response': 'Either username or password are incorrect',
            'status_code': 400,
        }

        # Act
        response = presenter.login_failed_response()

        # Arrange
        assert response == expected_response
