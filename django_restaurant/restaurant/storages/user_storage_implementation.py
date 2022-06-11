from typing import Union

from restaurant.interactors.storages.dtos import AddUserDetailsDTO, UserDetailsDTO
from restaurant.interactors.storages.user_storages_interface import UserStorageInterface


class UserStorageImplementation(UserStorageInterface):

    def check_user_exists(self, user_id: str):
        from restaurant.models import User

        return User.objects.filter(id=user_id).exists()

    def is_mobile_number_already_registered(self, mobile_number: str):
        from restaurant.models import User

        return User.objects.filter(mobile_number=mobile_number).exists()

    def check_username_already_exists(self, username: str) -> bool:
        from restaurant.models import User

        return User.objects.filter(username=username).exists()

    def add_user(self, user_details_dto: AddUserDetailsDTO):
        user_obj = self._create_user_obj(user_details_dto=user_details_dto)
        user_obj.save()
        return user_obj.id

    @staticmethod
    def _create_user_obj(user_details_dto: AddUserDetailsDTO):
        from restaurant.models import User
        from django.contrib.auth.hashers import make_password

        import datetime
        user_obj = User(
            id=user_details_dto.id,
            username=user_details_dto.username,
            first_name=user_details_dto.first_name,
            mobile_number=user_details_dto.mobile_number,
            last_name=user_details_dto.last_name,
            password=make_password(user_details_dto.password),
            is_staff=user_details_dto.is_staff,
            is_active=user_details_dto.is_active,
            date_joined=datetime.datetime.now(),
        )
        return user_obj

    def get_user(self, user_id) -> UserDetailsDTO:
        from restaurant.models import User
        from restaurant.exceptions.exceptions import UserNotFoundException

        if not User.objects.filter(id=user_id).exists():
            raise UserNotFoundException()
        user_details = User.objects.get(id=user_id)
        user_dto = self._get_user_details_dto(user_details)
        return user_dto

    @staticmethod
    def _get_user_details_dto(user_details) -> UserDetailsDTO:
        user_dto = UserDetailsDTO(
            id=str(user_details.id),
            username=str(user_details.username),
            first_name=user_details.first_name,
            last_name=user_details.last_name,
            mobile_number=user_details.mobile_number,
            date_joined=str(user_details.date_joined.replace(tzinfo=None)),
        )
        return user_dto

    def authenticate_user(self, user_dto) -> (Union[str, None], bool):
        pass
