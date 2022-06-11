from restaurant.exceptions.exceptions import MobileNumberAlreadyRegisteredException, UsernameAlreadyTakenException, \
    WeakPasswordException
from restaurant.interactors.presenters.presenter_interface import PresenterInterface
from restaurant.interactors.storages.dtos import AddUserDetailsDTO
from restaurant.interactors.storages.user_storages_interface import UserStorageInterface
from restaurant.interactors.validation_mixin import ValidationMixin


class AddUserDetailsInteractor(ValidationMixin):
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def sign_up_wrapper(
            self, user_details_dto: AddUserDetailsDTO,
            presenter: PresenterInterface
    ):
        try:
            user_dto = self.sign_up_user(user_details_dto=user_details_dto)
            return presenter.add_user_details_success_response(user_dto=user_dto)
        except MobileNumberAlreadyRegisteredException:
            return presenter.mobile_number_already_registered_response(
                mobile_number=user_details_dto.mobile_number
            )
        except UsernameAlreadyTakenException:
            return presenter.username_already_taken_response(
                username=user_details_dto.username
            )
        except WeakPasswordException:
            return presenter.weak_password_exception_response()

    def sign_up_user(self, user_details_dto: AddUserDetailsDTO):
        self.validate_mobile_number(
            mobile_number=user_details_dto.mobile_number, user_storage=self.user_storage
        )
        if self.check_username_exists(
                user_storage=self.user_storage, username=user_details_dto.username
        ):
            raise UsernameAlreadyTakenException()
        self.validate_password_pattern(password=user_details_dto.password)
        user_id = self.user_storage.add_user(user_details_dto=user_details_dto)
        user_dto = self.user_storage.get_user(user_id=user_id)

        return user_dto