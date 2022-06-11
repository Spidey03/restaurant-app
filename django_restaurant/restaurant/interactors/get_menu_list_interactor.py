from typing import List

from restaurant.interactors.presenters.presenter_interface import PresenterInterface
from restaurant.interactors.storages.dtos import ItemDTO
from restaurant.interactors.storages.restaurant_storage_interface import RestaurantStorageInterface


class GetMenuInteractor:
    def __init__(self, restaurant_storage: RestaurantStorageInterface):
        self.restaurant_storage = restaurant_storage

    def get_menu_wrapper(self, presenter: PresenterInterface):
        menu_items_dto = self._get_menu()
        return presenter.get_menu_items_response(
            menu_items_dto_list=menu_items_dto
        )

    def _get_menu(self) -> List[ItemDTO]:
        menu_items_dto_list = self.restaurant_storage.get_menu_items()
        return menu_items_dto_list
