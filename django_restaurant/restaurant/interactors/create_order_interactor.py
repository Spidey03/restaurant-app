from typing import List

from restaurant.exceptions.exceptions import TableNotFoundException, ItemIdNotFoundException
from restaurant.interactors.presenters.presenter_interface import PresenterInterface
from restaurant.interactors.storages.restaurant_storage_interface import RestaurantStorageInterface


class CreateOrderInteractor:
    def __init__(
        self,
        restaurant_storage: RestaurantStorageInterface
    ):
        self.restaurant_storage = restaurant_storage

    def create_order_wrapper(
        self, user_id: str, table_id: str,
        items: List[str], presenter: PresenterInterface
    ):
        try:
            order_id = self._create_order(
                user_id=user_id, table_id=table_id, items=items
            )
            presenter.order_created_successfully(order_id=order_id)
        except TableNotFoundException:
            presenter.table_not_found_response(table_id=table_id)
        except ItemIdNotFoundException as item_exc:
            presenter.items_not_found(item_ids=item_exc.item_ids)

    def _create_order(self, user_id: str, table_id: str, items: List[str]):
        if not self.restaurant_storage.validate_table_id(table_id=table_id):
            raise TableNotFoundException()
        valid_item_ids = self.restaurant_storage.validate_item_ids(item_ids=items)
        invalid_item_ids = list(set(items) - set(valid_item_ids))
        if invalid_item_ids:
            raise ItemIdNotFoundException(item_ids=invalid_item_ids)
        order_id = self.restaurant_storage.create_order(item_ids=items)
        self.restaurant_storage.create_table_order(
            table_id=table_id, user_id=user_id, order_id=order_id
        )
        return order_id
