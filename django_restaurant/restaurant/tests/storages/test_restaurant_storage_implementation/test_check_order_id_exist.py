import factory
import pytest

from restaurant.storages.restaurant_storage_implementation import RestaurantStorageImplementation
from restaurant.tests.common_fixtures.model_factories import ItemModelFactory, TableModelFactory, OrderModelFactory, \
    TableOrderModelFactory
from restaurant.tests.common_fixtures.reset_sequence import reset


class TestCheckOrderIDExist:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = RestaurantStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def table_order(self):
        reset()
        TableOrderModelFactory.create()

    @pytest.mark.django_db
    def test_when_order_not_exists(self, storage, table_order):
        # Arrange
        order_id = 'd32b2f96-93f5-4e2f-842d-d590783dc001'

        # Act
        response = storage.check_order_id_exist(order_id=order_id)

        # Assert
        assert response is False

    @pytest.mark.django_db
    def test_when_order_exists(self, storage, table_order):
        # Arrange
        order_id = 'd32b2f96-93f5-4e2f-842d-d590783dc000'

        # Act
        response = storage.check_order_id_exist(order_id=order_id)

        # Assert
        assert response is True
