import abc
from typing import List

from restaurant.interactors.storages.dtos import ItemDTO


class RestaurantStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_menu_items(self) -> List[ItemDTO]:
        pass
