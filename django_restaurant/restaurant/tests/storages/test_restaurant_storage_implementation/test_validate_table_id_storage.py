import pytest

from restaurant.storages.restaurant_storage_implementation import RestaurantStorageImplementation
from restaurant.tests.common_fixtures.model_factories import ItemModelFactory, TableModelFactory
from restaurant.tests.common_fixtures.reset_sequence import reset


TABLE_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'


class TestValidateTableID:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = RestaurantStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def table_db(self):
        reset()
        TableModelFactory.create(id=TABLE_ID)

    @pytest.mark.django_db
    def test_when_table_not_exist(self, storage, table_db):
        # Arrange
        table_id = 'd32b2f96-93f5-4e2f-842d-d590783dc002'

        # Act
        response = storage.validate_table_id(table_id=table_id)

        # Assert
        assert response is False

    @pytest.mark.django_db
    def test_when_table_exist(self, storage, table_db):
        # Arrange

        # Act
        response = storage.validate_table_id(table_id=TABLE_ID)

        # Assert
        assert response is True
