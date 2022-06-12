import datetime
from unittest.mock import create_autospec, Mock, patch

import pytest

from common.services.oauth2_service import Oauth2Service
from common.storage_implementation.dtos import UserAuthTokensDTO
from restaurant.tests.common_fixtures.reset_sequence import reset

USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'
TABLE_ID = 'e32b2f96-93f5-4e2f-842d-d590783dc001'
ITEM_IDS = [
    'f32b2f96-93f5-4e2f-842d-d590783dc000',
    'f32b2f96-93f5-4e2f-842d-d590783dc001'
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
        from restaurant.interactors.create_order_interactor import CreateUpdateOrderInteractor
        return CreateUpdateOrderInteractor(
            restaurant_storage=restaurant_storage
        )

    @pytest.fixture
    def presenter(self):
        from restaurant.interactors.presenters.presenter_interface import PresenterInterface

        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def item_dtos(self):
        reset()
        from restaurant.tests.common_fixtures.factories import ItemDTOFactory
        return ItemDTOFactory.create_batch(size=2)

    def test_when_items_not_selected(
            self, restaurant_storage, presenter, interactor
    ):
        # Arrange
        presenter.no_items_selected_response.return_value = Mock()

        # Act
        interactor.create_update_order_wrapper(
            order_id='',
            user_id=USER_ID,
            table_id=TABLE_ID,
            items=[],
            presenter=presenter
        )

        # Assert
        presenter.no_items_selected_response.assert_called_once()

    def test_when_table_not_exist(
            self, restaurant_storage, presenter, interactor
    ):
        # Arrange
        restaurant_storage.validate_table_id.return_value = False
        presenter.table_not_found_response.return_value = Mock()

        # Act
        interactor.create_update_order_wrapper(
            order_id='',
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
            self, restaurant_storage, presenter, interactor, item_dtos
    ):
        # Arrange
        restaurant_storage.validate_table_id.return_value = True
        restaurant_storage.validate_item_objs.return_value = item_dtos
        presenter.items_not_found.return_value = Mock()

        # Act
        interactor.create_update_order_wrapper(
            order_id='',
            user_id=USER_ID,
            table_id=TABLE_ID,
            items=ITEM_IDS,
            presenter=presenter
        )

        # Assert
        restaurant_storage.validate_table_id.assert_called_once_with(table_id=TABLE_ID)
        restaurant_storage.validate_item_objs.assert_called_once_with(item_ids=ITEM_IDS)
        presenter.items_not_found.assert_called_once()

    def test_when_create_order_successful(
            self, restaurant_storage, presenter, interactor, item_dtos
    ):
        # Arrange
        ORDER_ID = 'g32b2f96-93f5-4e2f-842d-d590783dc001'
        item_ids = [
            'd32b2f96-93f5-4e2f-842d-d590783dc000',
            'd32b2f96-93f5-4e2f-842d-d590783dc001'
        ]

        restaurant_storage.validate_table_id.return_value = True
        restaurant_storage.validate_item_objs.return_value = item_dtos
        restaurant_storage.create_order.return_value = ORDER_ID
        restaurant_storage.create_table_order.return_value = Mock()
        presenter.order_created_successfully.return_value = Mock()

        # Act
        interactor.create_update_order_wrapper(
            order_id='',
            user_id=USER_ID,
            table_id=TABLE_ID,
            items=item_ids,
            presenter=presenter
        )

        # Assert
        restaurant_storage.validate_table_id.assert_called_once_with(table_id=TABLE_ID)
        restaurant_storage.validate_item_objs.assert_called_once_with(item_ids=item_ids)
        restaurant_storage.create_order.assert_called_once_with(item_ids=item_ids, amount=6000)
        restaurant_storage.create_table_order.assert_called_once_with(
            table_id=TABLE_ID, user_id=USER_ID, order_id=ORDER_ID
        )
        presenter.order_created_successfully.assert_called_once_with(
            order_id=ORDER_ID
        )

    def test_update_order(
            self, restaurant_storage, presenter, interactor, item_dtos
    ):
        # Arrange
        ORDER_ID = 'g32b2f96-93f5-4e2f-842d-d590783dc001'
        item_ids = [
            'd32b2f96-93f5-4e2f-842d-d590783dc000',
            'd32b2f96-93f5-4e2f-842d-d590783dc001'
        ]

        restaurant_storage.validate_table_id.return_value = True
        restaurant_storage.validate_item_objs.return_value = item_dtos
        restaurant_storage.check_order_id_exist.return_value = True
        restaurant_storage.update_order.return_value = ORDER_ID
        restaurant_storage.create_table_order.return_value = Mock()
        presenter.order_created_successfully.return_value = Mock()

        # Act
        interactor.create_update_order_wrapper(
            order_id=ORDER_ID,
            user_id=USER_ID,
            table_id=TABLE_ID,
            items=item_ids,
            presenter=presenter
        )

        # Assert
        restaurant_storage.validate_table_id.assert_called_once_with(table_id=TABLE_ID)
        restaurant_storage.validate_item_objs.assert_called_once_with(item_ids=item_ids)
        restaurant_storage.check_order_id_exist.assert_called_once_with(order_id=ORDER_ID)
        restaurant_storage.update_order.assert_called_once_with(
            order_id=ORDER_ID, item_ids=item_ids, amount=6000
        )
        presenter.order_created_successfully.assert_called_once_with(
            order_id=ORDER_ID
        )