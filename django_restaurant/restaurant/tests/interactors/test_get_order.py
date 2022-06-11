from unittest.mock import create_autospec, Mock

import pytest

from restaurant.tests.common_fixtures.factories import UserDTOFactory, OrderDTOFactory, ItemDTOFactory, \
    TableOrderDTOFactory
from restaurant.tests.common_fixtures.reset_sequence import reset

USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'
ORDER_ID = 'e32b2f96-93f5-4e2f-842d-d590783dc001'


class TestGetOrderInteractor:
    @pytest.fixture
    def user_storage(self):
        from restaurant.interactors.storages.user_storages_interface import UserStorageInterface

        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def restaurant_storage(self):
        from restaurant.interactors.storages.restaurant_storage_interface import (
            RestaurantStorageInterface,
        )

        storage = create_autospec(RestaurantStorageInterface)
        return storage

    @pytest.fixture
    def interactor(self, restaurant_storage, user_storage):
        from restaurant.interactors.get_order_details import GetOrderInteractor
        return GetOrderInteractor(
            user_storage=user_storage,
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
            self, restaurant_storage, presenter, interactor, user_storage
    ):
        # Arrange
        restaurant_storage.check_order_id_exist.return_value = False
        presenter.no_items_selected_response.return_value = Mock()

        # Act
        interactor.get_order_details_wrapper(
            user_id=USER_ID,
            order_id=ORDER_ID,
            presenter=presenter
        )

        # Assert
        restaurant_storage.check_order_id_exist.assert_called_once_with(
            order_id=ORDER_ID
        )
        presenter.order_not_found.assert_called_once_with(order_id=ORDER_ID)

    def test_when_user_is_not_owner_and_not_admin(
            self, restaurant_storage, presenter, interactor, user_storage
    ):
        # Arrange
        restaurant_storage.check_order_id_exist.return_value = True
        from restaurant.tests.common_fixtures.factories import TableOrderDTOFactory
        restaurant_storage.get_table_order.return_value = TableOrderDTOFactory(
            user_id='d32b2f96-93f5-4e2f-842d-d590783dc002'
        )
        user_storage.is_user_admin.return_value = False
        presenter.user_dont_have_access.return_value = Mock()

        # Act
        interactor.get_order_details_wrapper(
            user_id=USER_ID,
            order_id=ORDER_ID,
            presenter=presenter
        )

        # Assert
        restaurant_storage.check_order_id_exist.assert_called_once_with(
            order_id=ORDER_ID
        )
        restaurant_storage.get_table_order.assert_called_once_with(
            order_id=ORDER_ID
        )
        user_storage.is_user_admin.assert_called_once_with(
            user_id=USER_ID
        )
        presenter.user_dont_have_access.assert_called_once()

    def test_when_user_is_not_owner_but_admin(
            self, restaurant_storage, presenter, interactor, user_storage
    ):
        # Arrange
        restaurant_storage.check_order_id_exist.return_value = True
        from restaurant.tests.common_fixtures.factories import TableOrderDTOFactory
        restaurant_storage.get_table_order.return_value = TableOrderDTOFactory(
            user_id='d32b2f96-93f5-4e2f-842d-d590783dc002'
        )
        user_storage.is_user_admin.return_value = True
        presenter.user_dont_have_access.return_value = Mock()

        # Act
        interactor.get_order_details_wrapper(
            user_id=USER_ID,
            order_id=ORDER_ID,
            presenter=presenter
        )

        # Assert
        restaurant_storage.check_order_id_exist.assert_called_once_with(
            order_id=ORDER_ID
        )
        restaurant_storage.get_table_order.assert_called_once_with(
            order_id=ORDER_ID
        )
        user_storage.is_user_admin.assert_called_once_with(
            user_id=USER_ID
        )
        presenter.user_dont_have_access.assert_not_called()

    def test_success_response(
            self, restaurant_storage, presenter, interactor, user_storage
    ):
        # Arrange
        reset()
        user_dto = UserDTOFactory()
        order_dto = OrderDTOFactory()
        item_dtos = ItemDTOFactory.create_batch(size=2)
        restaurant_storage.check_order_id_exist.return_value = True
        restaurant_storage.get_table_order.return_value = TableOrderDTOFactory(
            user_id='d32b2f96-93f5-4e2f-842d-d590783dc001'
        )
        user_storage.is_user_admin.return_value = False
        user_storage.get_user.return_value = user_dto
        restaurant_storage.get_order.return_value = order_dto
        restaurant_storage.get_items.return_value = item_dtos
        presenter.user_dont_have_access.return_value = Mock()

        # Act
        interactor.get_order_details_wrapper(
            user_id=USER_ID,
            order_id=ORDER_ID,
            presenter=presenter
        )

        # Assert
        restaurant_storage.check_order_id_exist.assert_called_once_with(
            order_id=ORDER_ID
        )
        restaurant_storage.get_table_order.assert_called_once_with(
            order_id=ORDER_ID
        )
        user_storage.get_user.assert_called_once_with(user_id=USER_ID)
        restaurant_storage.get_order.assert_called_once_with(order_id=ORDER_ID)
        restaurant_storage.get_items.assert_called_once()
        presenter.get_order_response.assert_called_once_with(
            user_dto=user_dto, order_dto=order_dto, item_dtos=item_dtos
        )
