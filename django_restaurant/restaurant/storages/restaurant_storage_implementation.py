from typing import List

from restaurant.interactors.storages.dtos import ItemDTO, TableOrderDTO, OrderDTO
from restaurant.interactors.storages.restaurant_storage_interface import RestaurantStorageInterface


class RestaurantStorageImplementation(RestaurantStorageInterface):

    def get_menu_items(self) -> List[ItemDTO]:
        from restaurant.models import Item

        item_objs = Item.objects.all()
        return self._create_item_dtos(item_objs)

    def _create_item_dtos(self, item_objs):
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
        return self._create_item_dtos(item_objs)

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
            table_id=table_id,
            user_id=user_id,
            order_id=order_id
        )

    def get_table_order(self, order_id: str) -> TableOrderDTO:
        from restaurant.models import TableOrder
        tb_obj = TableOrder.objects.filter(order_id=order_id)[0]
        return TableOrderDTO(
            id=str(tb_obj.id),
            user_id=str(tb_obj.user_id),
            table_id=str(tb_obj.table_id),
            order_id=str(tb_obj.order_id),
        )

    def get_order(self, order_id: str) -> OrderDTO:
        from restaurant.models import Order
        order_obj = Order.objects.filter(id=order_id).prefetch_related('items')[0]
        return OrderDTO(
            id=str(order_obj.id),
            is_paid=order_obj.is_paid,
            amount=order_obj.amount,
            items=[str(item.id) for item in order_obj.items.all()]
        )

    def get_items(self, item_ids: List[str]) -> List[ItemDTO]:
        from restaurant.models import Item
        item_objs = Item.objects.filter(id__in=item_ids)
        return self._create_item_dtos(item_objs)

    def check_order_id_exist(self, order_id: str) -> bool:
        from restaurant.models import Order
        return Order.objects.filter(id=order_id).exists()

    def update_order(self, order_id, item_ids, amount):
        from restaurant.models import Order

        Order.objects.filter(id=order_id).update(amount=amount)
        order = Order.objects.get(id=order_id)
        order.items.set(item_ids)
        order.save()
        return str(order.id)