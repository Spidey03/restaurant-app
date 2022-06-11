from typing import Optional

from restaurant.interactors.storages.user_storages_interface import UserStorageInterface


class ValidationMixin:

    @staticmethod
    def validate_mobile_number(mobile_number, user_storage: UserStorageInterface):
        from restaurant.exceptions.exceptions import MobileNumberAlreadyRegisteredException

        is_exists = user_storage.is_mobile_number_already_registered(
            mobile_number=mobile_number
        )
        if is_exists:
            raise MobileNumberAlreadyRegisteredException()

    @staticmethod
    def validate_password_pattern(password: str):
        import re
        from restaurant.exceptions.exceptions import WeakPasswordException

        regex = re.compile(
            r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
        )
        if not re.fullmatch(regex, password):
            raise WeakPasswordException()

    @staticmethod
    def check_username_exists(
        user_storage: UserStorageInterface, username: str
    ) -> bool:
        return user_storage.check_username_already_exists(username=username)
