from typing import List


class UserNotFoundException(Exception):
    pass


class WeakPasswordException(Exception):
    def __str__(self):
        return 'Weak password: A minimum 8 characters password contains a combination of uppercase and lowercase letter and number'

    pass


class MobileNumberAlreadyRegisteredException(Exception):
    pass


class UserNotExistsException(Exception):
    pass


class UsernameAlreadyTakenException(Exception):
    pass


class UsernameNotFoundException(Exception):
    pass


class LoginFailedException(Exception):
    pass


class TableNotFoundException(Exception):
    pass


class ItemIdNotFoundException(Exception):
    def __init__(self, item_ids: List[str]):
        self.item_ids = item_ids


class NoItemsHaveSelectedException(Exception):
    pass


class OrderNotFoundException(Exception):
    def __init__(self, order_id: str):
        self.order_id = order_id

class UserDonnotHaveAccessException(Exception):
    pass