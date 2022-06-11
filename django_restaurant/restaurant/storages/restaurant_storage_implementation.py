from typing import List

from restaurant.interactors.storages.dtos import ItemDTO
from restaurant.interactors.storages.restaurant_storage_interface import RestaurantStorageInterface


class RestaurantStorageImplementation(RestaurantStorageInterface):

    def get_menu_items(self) -> List[ItemDTO]:
        from restaurant.models import Item

        item_objs = Item.objects.all()
        return [
            ItemDTO(
                id=item_obj.id,
                name=item_obj.name,
                price=item_obj.price,
                description=item_obj.description,
            ) for item_obj in item_objs
        ]

    def validate_table_id(self, table_id):
        pass

    def validate_item_ids(self, item_ids):
        pass

    def create_order(self, item_ids):
        pass

    def create_table_order(
            self, table_id: str, user_id: str, order_id: str
    ):
        pass
