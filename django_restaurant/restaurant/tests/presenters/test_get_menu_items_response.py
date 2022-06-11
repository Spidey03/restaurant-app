import pytest

from restaurant.tests.common_fixtures.factories import UserDetailsDTOFactory, ItemDTOFactory
from restaurant.tests.common_fixtures.reset_sequence import reset


class TestGetMenuItemsResponse:
    @pytest.fixture
    def presenter(self):
        from restaurant.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    @pytest.fixture
    def item_dtos(self):
        reset()
        return ItemDTOFactory.create_batch(size=2)

    def test_get_menu_items_response(self, presenter, item_dtos):
        # Arrange

        expected_response = [
            {
                'description': '',
                'id': 'd32b2f96-93f5-4e2f-842d-d590783dc000',
                'name': 'Item 0',
                'price': 3000
            },
            {
                'description': '',
                'id': 'd32b2f96-93f5-4e2f-842d-d590783dc001',
                'name': 'Item 1',
                'price': 3000
            }
        ]
        # Act
        response = presenter.get_menu_items_response(
            menu_items_dto_list=item_dtos
        )

        # Arrange
        assert response == expected_response
