import factory
import pytest

from restaurant.storages.restaurant_storage_implementation import RestaurantStorageImplementation
from restaurant.tests.common_fixtures.model_factories import ItemModelFactory, TableModelFactory
from restaurant.tests.common_fixtures.reset_sequence import reset

ITEMS_ID = [
    'd32b2f96-93f5-4e2f-842d-d590783dc000',
    'd32b2f96-93f5-4e2f-842d-d590783dc001',
]

class TestCreateOrder:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = RestaurantStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def items_db(self):
        reset()
        ItemModelFactory.create_batch(
            id=factory.Iterator(ITEMS_ID), size=len(ITEMS_ID)
        )

    @pytest.mark.django_db
    def test_create_order(self, storage, items_db):
        # Arrange
        amount = 500

        # Act
        order_id = storage.create_order(item_ids=ITEMS_ID, amount=amount)

        # Assert
        from restaurant.models import Order
        order_obj = Order.objects.get(id=order_id)
        assert str(order_obj.id) == order_id
        assert order_obj.amount == amount
        assert len(order_obj.items.all()) == len(ITEMS_ID)