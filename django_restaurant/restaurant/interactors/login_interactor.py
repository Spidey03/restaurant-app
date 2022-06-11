from restaurant.exceptions.exceptions import UsernameNotFoundException, LoginFailedException
from restaurant.interactors.presenters.presenter_interface import PresenterInterface
from restaurant.interactors.storages.dtos import LoginUserDTO
from restaurant.interactors.storages.user_storages_interface import UserStorageInterface
from restaurant.interactors.validation_mixin import ValidationMixin


class LoginInteractor(ValidationMixin):
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def login_wrapper(
        self, login_user_dto: LoginUserDTO,
        presenter: PresenterInterface
    ):
        try:
            self._login_user(login_user_dto=login_user_dto)
        except UsernameNotFoundException:
            presenter.username_not_found_response(username=login_user_dto.username)
        except LoginFailedException:
            presenter.login_failed_response()

    def _login_user(self, login_user_dto: LoginUserDTO):
        username_not_fount = not self.check_username_exists(
            user_storage=self.user_storage, username=login_user_dto.username
        )
        if username_not_fount:
            raise UsernameNotFoundException()
        user_id, authenticated = self.user_storage.authenticate_user(user_dto=login_user_dto)

        if not authenticated:
            raise LoginFailedException()