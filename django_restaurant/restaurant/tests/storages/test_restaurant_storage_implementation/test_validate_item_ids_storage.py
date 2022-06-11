import pytest

from restaurant.storages.restaurant_storage_implementation import RestaurantStorageImplementation
from restaurant.tests.common_fixtures.model_factories import ItemModelFactory, TableModelFactory
from restaurant.tests.common_fixtures.reset_sequence import reset


class TestValidateItemIDs:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = RestaurantStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def items_db(self):
        reset()
        ItemModelFactory.create_batch(size=2)

    @pytest.fixture
    def item_dtos(self):
        reset()
        from restaurant.tests.common_fixtures.factories import ItemDTOFactory
        return ItemDTOFactory.create_batch(size=2)

    @pytest.mark.django_db
    def test_validate_item_ids(self, storage, items_db, item_dtos):
        # Arrange

        item_ids = [
            'd32b2f96-93f5-4e2f-842d-d590783dc010',
            'd32b2f96-93f5-4e2f-842d-d590783dc000',
            'd32b2f96-93f5-4e2f-842d-d590783dc001',
            'd32b2f96-93f5-4e2f-842d-d590783dc002',
        ]

        # Act
        response = storage.validate_item_objs(item_ids=item_ids)

        # Assert
        assert len(response) == len(item_dtos)
