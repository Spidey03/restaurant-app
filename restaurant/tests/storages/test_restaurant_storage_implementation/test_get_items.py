import factory
import pytest

from restaurant.storages.restaurant_storage_implementation import RestaurantStorageImplementation
from restaurant.tests.common_fixtures.model_factories import ItemModelFactory, TableModelFactory, OrderModelFactory, \
    TableOrderModelFactory
from restaurant.tests.common_fixtures.reset_sequence import reset


class TestGetItems:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = RestaurantStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def db(self):
        reset()
        ItemModelFactory.create_batch(size=3)

    @pytest.mark.django_db
    def test_get_items(self, storage, db):
        # Arrange
        item_ids = [
            'd32b2f96-93f5-4e2f-842d-d590783dc000',
            'd32b2f96-93f5-4e2f-842d-d590783dc002'
        ]

        # Act
        response = storage.get_items(item_ids=item_ids)

        # Assert
        assert len(response) is 2
