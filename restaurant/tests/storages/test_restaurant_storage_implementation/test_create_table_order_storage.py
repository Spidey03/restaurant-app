import factory
import pytest

from restaurant.storages.restaurant_storage_implementation import RestaurantStorageImplementation
from restaurant.tests.common_fixtures.model_factories import ItemModelFactory, TableModelFactory, UserModelFactory, \
    OrderModelFactory
from restaurant.tests.common_fixtures.reset_sequence import reset

USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'
TABLE_ID = 'f32b2f96-93f5-4e2f-842d-d590783dc001'
ORDER_ID = 'e32b2f96-93f5-4e2f-842d-d590783dc001'


class TestCreateTableOrder:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = RestaurantStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def order_db(self):
        reset()
        UserModelFactory.create(id=USER_ID)
        TableModelFactory.create(id=TABLE_ID)
        OrderModelFactory.create(id=ORDER_ID)

    @pytest.mark.django_db
    def test_create_table_order(self, storage, order_db):
        # Arrange

        # Act
        storage.create_table_order(
            user_id=USER_ID,
            table_id=TABLE_ID,
            order_id=ORDER_ID
        )

        # Assert
        from restaurant.models import TableOrder
        assert TableOrder.objects.filter(
            user_id=USER_ID,
            table_id=TABLE_ID,
            order_id=ORDER_ID
        ).exists() is True