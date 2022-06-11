from typing import List, Tuple

from restaurant.exceptions.exceptions import NoItemsHaveSelectedException, OrderNotFoundException, \
    UserDonNotHaveAccessException
from restaurant.interactors.presenters.presenter_interface import PresenterInterface
from restaurant.interactors.storages.dtos import OrderDTO, ItemDTO, UserDetailsDTO
from restaurant.interactors.storages.restaurant_storage_interface import RestaurantStorageInterface
from restaurant.interactors.storages.user_storages_interface import UserStorageInterface


class GetOrderInteractor:
    def __init__(
            self,
            user_storage: UserStorageInterface,
            restaurant_storage: RestaurantStorageInterface
    ):
        self.user_storage = user_storage
        self.restaurant_storage = restaurant_storage

    def get_order_details_wrapper(
            self, order_id: str, user_id: str, presenter: PresenterInterface
    ):
        try:
            user_dto, order_dto, item_dtos = self._get_order_details(
                user_id=user_id, order_id=order_id
            )
            return presenter.get_order_response(
                user_dto=user_dto, order_dto=order_dto, item_dtos=item_dtos
            )
        except OrderNotFoundException as e:
            return presenter.order_not_found(order_id=e.order_id)
        except UserDonNotHaveAccessException as item_exc:
            return presenter.user_dont_have_access()
        except NoItemsHaveSelectedException:
            return presenter.no_items_selected_response()

    def _get_order_details(self, user_id, order_id) -> Tuple[UserDetailsDTO, OrderDTO, List[ItemDTO]]:
        if not self.restaurant_storage.check_order_id_exist(order_id=order_id):
            raise OrderNotFoundException(order_id=order_id)
        table_order_dto = self.restaurant_storage.get_table_order(order_id=order_id)
        if not (user_id == table_order_dto.user_id or self.user_storage.is_user_admin(user_id=user_id)):
            raise UserDonNotHaveAccessException()

        user_dto = self.user_storage.get_user(user_id=user_id)
        order_dto = self.restaurant_storage.get_order(order_id=order_id)
        item_ids = order_dto.items
        item_dtos = self.restaurant_storage.get_items(item_ids=item_ids)
        return user_dto, order_dto, item_dtos
