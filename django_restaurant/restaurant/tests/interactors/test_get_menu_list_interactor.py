import datetime
from unittest.mock import create_autospec, Mock, patch

import pytest

from common.services.oauth2_service import Oauth2Service
from common.storage_implementation.dtos import UserAuthTokensDTO
from restaurant.tests.common_fixtures.reset_sequence import reset


class TestGetSiteDetailsBulkInteractor:
    @pytest.fixture
    def restaurant_storage(self):
        from restaurant.interactors.storages.restaurant_storage_interface import (
            RestaurantStorageInterface,
        )

        storage = create_autospec(RestaurantStorageInterface)
        return storage

    @pytest.fixture
    def interactor(self, restaurant_storage):
        from restaurant.interactors.get_menu_list_interactor import GetMenuInteractor
        return GetMenuInteractor(restaurant_storage=restaurant_storage)

    @pytest.fixture
    def presenter(self):
        from restaurant.interactors.presenters.presenter_interface import PresenterInterface

        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def menu_items_dto_list(self):
        from restaurant.tests.common_fixtures.factories import ItemDTOFactory
        return ItemDTOFactory.create_batch(size=3)

    def test_get_menu_list(
            self, restaurant_storage, presenter, interactor, menu_items_dto_list
    ):
        # Arrange
        restaurant_storage.get_menu_items.return_value = menu_items_dto_list
        presenter.get_menu_items_response.return_value = Mock()

        # Act
        interactor.get_menu_wrapper(presenter=presenter)

        # Assert
        restaurant_storage.get_menu_items.assert_called_once()
        presenter.get_menu_items_response.assert_called_once_with(
            menu_items_dto_list=menu_items_dto_list
        )