import datetime
from unittest.mock import create_autospec, Mock

import pytest

from common.storage_implementation.dtos import UserAuthTokensDTO
from restaurant.tests.common_fixtures.factories import AddUserDetailsDTOFactory
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
        from restaurant.interactors.sign_up_interactor import (
            AddUserDetailsInteractor,
        )

        return AddUserDetailsInteractor(user_storage=user_storage)

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
    def user_details_dto(self):
        reset()
        return AddUserDetailsDTOFactory()

    def test_mobile_number_already_registered(
        self, user_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        user_storage.is_mobile_number_already_registered.return_value = True
        presenter.mobile_number_already_registered_response.return_value = Mock()

        # Act
        interactor.sign_up_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        user_storage.is_mobile_number_already_registered.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )
        presenter.mobile_number_already_registered_response.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )

    def test_when_username_already_taken(
        self, user_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        user_storage.is_mobile_number_already_registered.return_value = False
        user_storage.check_username_already_exists.return_value = True

        presenter.weak_password_exception_response.return_value = Mock()

        # Act
        interactor.sign_up_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        user_storage.is_mobile_number_already_registered.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )
        user_storage.check_username_already_exists.assert_called_once_with(
            username=user_details_dto.username
        )
        presenter.username_already_taken_response.assert_called_once_with(
            username=user_details_dto.username
        )

    def test_weak_password(self, user_storage, presenter, interactor, user_details_dto):
        # Arrange
        user_storage.is_mobile_number_already_registered.return_value = False
        user_storage.check_username_already_exists.return_value = False
        presenter.weak_password_exception_response.return_value = Mock()

        # Act
        interactor.sign_up_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        user_storage.is_mobile_number_already_registered.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )
        presenter.weak_password_exception_response.assert_called_once()

    def test_success_response(
        self, user_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        user_details_dto.password = '1@M4tIsUWyI'
        user_storage.is_mobile_number_already_registered.return_value = False
        user_storage.check_username_already_exists.return_value = False
        user_storage.add_user.return_value = user_details_dto.id
        user_storage.get_user.return_value = user_details_dto

        # Act
        interactor.sign_up_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        user_storage.is_mobile_number_already_registered.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )
        user_storage.add_user.assert_called_once_with(user_details_dto=user_details_dto)
        user_storage.get_user.assert_called_once_with(user_id=user_details_dto.id)
        presenter.add_user_details_success_response.assert_called_once_with(
            user_dto=user_details_dto
        )
