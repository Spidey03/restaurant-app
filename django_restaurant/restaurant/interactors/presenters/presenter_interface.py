import abc


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
    def get_menu_items_response(self, menu_items_dto):
        pass
