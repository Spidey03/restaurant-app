import abc
from typing import List

from restaurant.interactors.storages.dtos import ItemDTO, UserDetailsDTO, OrderDTO


class PresenterInterface(abc.ABC):

    @abc.abstractmethod
    def add_user_details_success_response(self, user_dto):
        pass

    @abc.abstractmethod
    def mobile_number_already_registered_response(self, mobile_number):
        pass

    @abc.abstractmethod
    def username_already_taken_response(self, username):
        pass

    @abc.abstractmethod
    def weak_password_exception_response(self):
        pass

    @abc.abstractmethod
    def username_not_found_response(self, username):
        pass

    @abc.abstractmethod
    def login_failed_response(self):
        pass

    @abc.abstractmethod
    def login_successful_response(self, auth_token_dto):
        pass

    @abc.abstractmethod
    def get_menu_items_response(self, menu_items_dto_list: List[ItemDTO]):
        pass

    @abc.abstractmethod
    def order_created_successfully(self, order_id: str):
        pass

    @abc.abstractmethod
    def table_not_found_response(self, table_id: str):
        pass

    @abc.abstractmethod
    def items_not_found(self, item_ids: List[str]):
        pass

    @abc.abstractmethod
    def no_items_selected_response(self):
        pass

    @abc.abstractmethod
    def order_not_found(self, order_id: str):
        pass

    @abc.abstractmethod
    def user_dont_have_access(self):
        pass

    @abc.abstractmethod
    def get_order_response(
            self,
            user_dto: UserDetailsDTO,
            order_dto: OrderDTO,
            item_dtos: List[ItemDTO]
    ):
        pass
