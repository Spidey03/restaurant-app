import factory
import pytest

from restaurant.storages.restaurant_storage_implementation import RestaurantStorageImplementation
from restaurant.tests.common_fixtures.model_factories import ItemModelFactory, TableModelFactory, OrderModelFactory, \
    TableOrderModelFactory
from restaurant.tests.common_fixtures.reset_sequence import reset


class TestGetTableOrder:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = RestaurantStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def table_order(self):
        reset()
        TableOrderModelFactory.create()

    @pytest.mark.django_db
    def test_get_table_order(self, storage, table_order):
        # Arrange
        order_id = 'd32b2f96-93f5-4e2f-842d-d590783dc000'
        table_id = 'd32b2f96-93f5-4e2f-842d-d590783dc000'

        # Act
        table_order_dto = storage.get_table_order(order_id=order_id)

        # Assert
        assert table_order_dto.order_id == order_id
        assert table_order_dto.table_id == table_id
