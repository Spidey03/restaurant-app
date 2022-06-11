from restaurant.interactors.storages.dtos import AddUserDetailsDTO, UserDetailsDTO
from restaurant.interactors.storages.user_storages_interface import UserStorageInterface


class UserStorageImplementation(UserStorageInterface):

    def check_user_exists(self, user_id: str):
        pass

    def is_mobile_number_already_registered(self, mobile_number: str):
        from restaurant.models import User

        return User.objects.filter(mobile_number=mobile_number).exists()

    def check_username_already_exists(self, username: str) -> bool:
        from restaurant.models import User

        return User.objects.filter(username=username).exists()

    def add_user(self, user_details_dto: AddUserDetailsDTO):
        pass

    def get_user(self, user_id) -> UserDetailsDTO:
        pass
