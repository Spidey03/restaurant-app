import abc

from restaurant.interactors.storages.dtos import AddUserDetailsDTO


class UserStorageInterface(abc.ABC):

    @abc.abstractmethod
    def check_user_exists(self, user_id: str):
        pass

    @abc.abstractmethod
    def is_email_already_registered(self, email: str) -> bool:
        pass

    @abc.abstractmethod
    def add_user(self, user_details_dto: AddUserDetailsDTO):
        pass

    @abc.abstractmethod
    def get_user(self, user_id):
        pass
