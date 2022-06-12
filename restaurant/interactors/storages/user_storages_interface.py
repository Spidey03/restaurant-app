import abc
from typing import Union

from restaurant.interactors.storages.dtos import AddUserDetailsDTO, UserDetailsDTO


class UserStorageInterface(abc.ABC):

    @abc.abstractmethod
    def check_user_exists(self, user_id: str):
        pass

    @abc.abstractmethod
    def is_mobile_number_already_registered(self, mobile_number: str):
        pass

    @abc.abstractmethod
    def check_username_already_exists(self, username: str) -> bool:
        pass

    @abc.abstractmethod
    def add_user(self, user_details_dto: AddUserDetailsDTO):
        pass

    @abc.abstractmethod
    def get_user(self, user_id) -> UserDetailsDTO:
        pass

    @abc.abstractmethod
    def authenticate_user(self, user_dto) -> (Union[str, None], bool):
        pass

    @abc.abstractmethod
    def is_user_admin(self, user_id: str) -> bool:
        pass
