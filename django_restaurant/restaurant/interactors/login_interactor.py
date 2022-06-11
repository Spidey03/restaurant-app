from common.storage_implementation.dtos import UserAuthTokensDTO
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
            token_dto = self._login_user(login_user_dto=login_user_dto)
            presenter.login_successful_response(auth_token_dto=token_dto)
        except UsernameNotFoundException:
            presenter.username_not_found_response(username=login_user_dto.username)
        except LoginFailedException:
            presenter.login_failed_response()

    def _login_user(self, login_user_dto: LoginUserDTO):
        username_not_found = not self.check_username_exists(
            user_storage=self.user_storage, username=login_user_dto.username
        )
        if username_not_found:
            raise UsernameNotFoundException()
        user_id, authenticated = self.user_storage.authenticate_user(user_dto=login_user_dto)

        if not authenticated:
            raise LoginFailedException()
        return self._get_auth_tokens(user_id=user_id)

    @staticmethod
    def _get_auth_tokens(user_id: str) -> UserAuthTokensDTO:
        from common.storage_implementation.oauth2_storage_implementation import (
            Oauth2StorageImplementation,
        )
        from common.services.oauth2_service import Oauth2Service

        oauth2storage = Oauth2StorageImplementation()
        oauth2service = Oauth2Service(oauth2storage=oauth2storage)
        return oauth2service.create_auth_tokens(user_id=user_id)
