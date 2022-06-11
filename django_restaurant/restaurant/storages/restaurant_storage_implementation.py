from typing import List

from restaurant.interactors.storages.dtos import ItemDTO
from restaurant.interactors.storages.restaurant_storage_interface import RestaurantStorageInterface


class RestaurantStorageImplementation(RestaurantStorageInterface):

    def get_menu_items(self) -> List[ItemDTO]:
        from restaurant.models import Item

        item_objs = Item.objects.all()
        return self._create_item_dto(item_objs)

    def _create_item_dto(self, item_objs):
        return [
            ItemDTO(
                id=item_obj.id,
                name=item_obj.name,
                price=item_obj.price,
                description=item_obj.description,
            ) for item_obj in item_objs
        ]

    def validate_table_id(self, table_id: str) -> bool:
        from restaurant.models import Table
        return Table.objects.filter(id=table_id).exists()

    def validate_item_objs(self, item_ids: List[str]) -> List[ItemDTO]:
        from restaurant.models import Item
        item_objs = Item.objects.filter(id__in=item_ids)
        return self._create_item_dto(item_objs)

    def create_order(self, item_ids: List[str], amount: float) -> str:
        from restaurant.models import Order
        import uuid

        order = Order.objects.create(id=str(uuid.uuid4()), amount=amount)
        order.items.set(item_ids)
        order.save()
        return str(order.id)

    def create_table_order(
            self, table_id: str, user_id: str, order_id: str
    ):
        from restaurant.models import TableOrder
        import uuid
        TableOrder.objects.create(
            id=uuid.uuid4(),
            table_id_id=table_id,
            user_id_id=user_id,
            order_id_id=order_id
        )
