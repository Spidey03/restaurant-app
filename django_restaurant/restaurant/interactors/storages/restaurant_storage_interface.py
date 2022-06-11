import abc
from typing import List

from restaurant.interactors.storages.dtos import ItemDTO


class RestaurantStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_menu_items(self) -> List[ItemDTO]:
        pass

    @abc.abstractmethod
    def validate_table_id(self, table_id: str) -> bool:
        pass

    @abc.abstractmethod
    def validate_item_objs(self, item_ids: List[str]) -> List[ItemDTO]:
        pass

    @abc.abstractmethod
    def create_order(self, item_ids: List[str], amount: float) -> str:
        pass

    @abc.abstractmethod
    def create_table_order(
            self, table_id: str, user_id: str, order_id: str
    ):
        pass
