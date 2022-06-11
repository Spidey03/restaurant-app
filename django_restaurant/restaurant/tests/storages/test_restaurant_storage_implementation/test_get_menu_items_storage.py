import pytest

from restaurant.storages.restaurant_storage_implementation import RestaurantStorageImplementation
from restaurant.tests.common_fixtures.model_factories import ItemModelFactory
from restaurant.tests.common_fixtures.reset_sequence import reset


class TestAuthenticateUser:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = RestaurantStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def items_db(self):
        reset()

        ItemModelFactory(
            id='d32b2f96-93f5-4e2f-842d-d590783dc001',
            name='pizza',
            description='',
            price='200',
        )
        ItemModelFactory(
            id='d32b2f96-93f5-4e2f-842d-d590783dc002',
            name='burger',
            description='',
            price='150',
        )

    @pytest.mark.django_db
    def test_when_match_username_and_password(self, storage, items_db):
        # Arrange

        # Act
        response = storage.get_menu_items()

        # Assert
        assert len(response) == 2
