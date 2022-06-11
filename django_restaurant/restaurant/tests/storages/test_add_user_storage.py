import pytest

from restaurant.tests.common_fixtures.reset_sequence import reset


class TestAddSiteDetailsStorage:
    @pytest.fixture
    def storage(self):
        from restaurant.storages.user_storage_implementation import (
            UserStorageImplementation,
        )

        return UserStorageImplementation()

    @pytest.fixture
    def user_dto(self):
        from restaurant.tests.common_fixtures.factories import AddUserDetailsDTOFactory

        reset()
        user_dto = AddUserDetailsDTOFactory.create()
        return user_dto

    @pytest.mark.django_db
    def test_add_site_details(self, storage, user_dto):
        # Arrange
        user_id = user_dto.id

        # Act
        storage.add_user(user_details_dto=user_dto)

        # Assert
        from restaurant.models import User

        assert User.objects.filter(id=user_id).exists() is True
