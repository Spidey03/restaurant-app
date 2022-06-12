import datetime

import pytest

from restaurant.tests.common_fixtures.reset_sequence import reset


class TestUserDontHaveAccess:
    @pytest.fixture
    def presenter(self):
        from restaurant.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_user_dont_have_access(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'USER_DONT_HAVE_ACCESS',
            'response': "User don't have access",
            'status_code': 400
        }

        # Act
        response = presenter.user_dont_have_access()

        # Arrange
        assert response == expected_response
