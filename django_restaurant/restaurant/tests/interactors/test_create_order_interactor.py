import datetime
from unittest.mock import create_autospec, Mock, patch

import pytest

from common.services.oauth2_service import Oauth2Service
from common.storage_implementation.dtos import UserAuthTokensDTO
from restaurant.tests.common_fixtures.reset_sequence import reset

USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'
TABLE_ID = 'e32b2f96-93f5-4e2f-842d-d590783dc001'
ITEM_IDS = [
    'f32b2f96-93f5-4e2f-842d-d590783dc001',
    'f32b2f96-93f5-4e2f-842d-d590783dc002'
]


class TestCreateOrderInteractor:
    @pytest.fixture
    def restaurant_storage(self):
        from restaurant.interactors.storages.restaurant_storage_interface import (
            RestaurantStorageInterface,
        )

        storage = create_autospec(RestaurantStorageInterface)
        return storage

    @pytest.fixture
    def interactor(self, restaurant_storage):
        from restaurant.interactors.create_order_interactor import CreateOrderInteractor
        return CreateOrderInteractor(
            restaurant_storage=restaurant_storage
        )

    @pytest.fixture
    def presenter(self):
        from restaurant.interactors.presenters.presenter_interface import PresenterInterface

        presenter = create_autospec(PresenterInterface)
        return presenter

    def test_when_table_not_exist(
            self, restaurant_storage, presenter, interactor
    ):
        # Arrange
        restaurant_storage.validate_table_id.return_value = False
        presenter.table_not_found_response.return_value = Mock()

        # Act
        interactor.create_order_wrapper(
            user_id=USER_ID,
            table_id=TABLE_ID,
            items=ITEM_IDS,
            presenter=presenter
        )

        # Assert
        restaurant_storage.validate_table_id.assert_called_once_with(table_id=TABLE_ID)
        presenter.table_not_found_response.assert_called_once_with(
            table_id=TABLE_ID
        )

    def test_when_items_not_exist(
            self, restaurant_storage, presenter, interactor
    ):
        # Arrange
        restaurant_storage.validate_table_id.return_value = True
        restaurant_storage.validate_item_ids.return_value = ITEM_IDS[:1]
        presenter.items_not_found.return_value = Mock()

        # Act
        interactor.create_order_wrapper(
            user_id=USER_ID,
            table_id=TABLE_ID,
            items=ITEM_IDS,
            presenter=presenter
        )

        # Assert
        restaurant_storage.validate_table_id.assert_called_once_with(table_id=TABLE_ID)
        restaurant_storage.validate_item_ids.assert_called_once_with(item_ids=ITEM_IDS)
        presenter.items_not_found.assert_called_once_with(
            item_ids=ITEM_IDS[1:]
        )

    def test_when_create_order_successful(
            self, restaurant_storage, presenter, interactor
    ):
        # Arrange
        ORDER_ID = 'g32b2f96-93f5-4e2f-842d-d590783dc001'

        restaurant_storage.validate_table_id.return_value = True
        restaurant_storage.validate_item_ids.return_value = ITEM_IDS
        restaurant_storage.create_order.return_value = ORDER_ID
        restaurant_storage.create_table_order.return_value = Mock()
        presenter.order_created_successfully.return_value = Mock()

        # Act
        interactor.create_order_wrapper(
            user_id=USER_ID,
            table_id=TABLE_ID,
            items=ITEM_IDS,
            presenter=presenter
        )

        # Assert
        restaurant_storage.validate_table_id.assert_called_once_with(table_id=TABLE_ID)
        restaurant_storage.validate_item_ids.assert_called_once_with(item_ids=ITEM_IDS)
        restaurant_storage.create_order.assert_called_once_with(item_ids=ITEM_IDS)
        restaurant_storage.create_table_order.assert_called_once_with(
            table_id=TABLE_ID, user_id=USER_ID, order_id=ORDER_ID
        )
        presenter.order_created_successfully.assert_called_once_with(
            order_id=ORDER_ID
        )