import datetime
from unittest.mock import create_autospec, Mock, patch

import pytest

from common.services.oauth2_service import Oauth2Service
from common.storage_implementation.dtos import UserAuthTokensDTO
from restaurant.tests.common_fixtures.reset_sequence import reset

token_dto = UserAuthTokensDTO(
    user_id='f2c8cf25-10fe-4ce6-ba8b-1ab5fd355339',
    access_token='D5BlCiwEpQ6v7s9ykHIlgQlWSRelpt',
    refresh_token='OksuViZaG5dGTSI04mzQNADeUbM6zw',
    expires=datetime.datetime(2022, 5, 25, 15, 38, 46, 922544),
)


class TestGetSiteDetailsBulkInteractor:
    @pytest.fixture
    def user_storage(self):
        from restaurant.interactors.storages.user_storages_interface import (
            UserStorageInterface,
        )

        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def interactor(self, user_storage):
        from restaurant.interactors.login_interactor import LoginInteractor
        return LoginInteractor(user_storage=user_storage)

    @pytest.fixture
    def presenter(self):
        from restaurant.interactors.presenters.presenter_interface import PresenterInterface

        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def oauth2service(self):
        from common.services.oauth2_service import Oauth2Service
        from common.storage_implementation.oauth2_storage_implementation import (
            Oauth2StorageImplementation,
        )

        oauth2storage = Oauth2StorageImplementation()
        oauth2service = Oauth2Service(oauth2storage=oauth2storage)
        return oauth2service

    @pytest.fixture
    def login_user_dto(self):
        from restaurant.tests.common_fixtures.factories import LoginUserDTOFactory
        reset()
        return LoginUserDTOFactory.create()

    def test_when_username_not_found(
            self, user_storage, presenter, interactor, login_user_dto
    ):
        # Arrange
        user_storage.check_username_already_exists.return_value = False
        presenter.username_not_found_response = Mock()

        # Act
        interactor.login_wrapper(
            login_user_dto=login_user_dto, presenter=presenter
        )

        # Assert
        user_storage.check_username_already_exists.assert_called_once_with(
            username=login_user_dto.username
        )
        presenter.username_not_found_response.assert_called_once_with(
            username=login_user_dto.username
        )

    def test_when_authentication_failed(
            self, user_storage, presenter, interactor, login_user_dto
    ):
        # Arrange
        user_storage.check_username_already_exists.return_value = True
        user_storage.authenticate_user.return_value = (None, False)
        presenter.username_not_found_response = Mock()

        # Act
        interactor.login_wrapper(
            login_user_dto=login_user_dto, presenter=presenter
        )

        # Assert
        user_storage.check_username_already_exists.assert_called_once_with(
            username=login_user_dto.username
        )
        user_storage.authenticate_user.assert_called_once_with(
            user_dto=login_user_dto
        )
        presenter.login_failed_response.assert_called_once()

    @patch.object(Oauth2Service, 'create_auth_tokens', return_value=token_dto)
    def when_login_successful(
            self, user_storage, presenter, interactor, login_user_dto
    ):
        # Arrange
        USER_ID = 'f2c8cf25-10fe-4ce6-ba8b-1ab5fd355339'

        user_storage.check_username_already_exists.return_value = True
        user_storage.authenticate_user.return_value = (USER_ID, True)
        presenter.username_not_found_response = Mock()

        # Act
        interactor.login_wrapper(
            login_user_dto=login_user_dto, presenter=presenter
        )

        # Assert
        user_storage.check_username_already_exists.assert_called_once_with(
            username=login_user_dto.username
        )
        user_storage.authenticate_user.assert_called_once_with(
            user_dto=login_user_dto
        )
        presenter.login_successful_response.assert_called_once_with(auth_token_dto=token_dto)