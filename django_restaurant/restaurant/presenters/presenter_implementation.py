from restaurant.interactors.presenters.presenter_interface import PresenterInterface


class PresenterImplementation(PresenterInterface):
    def add_user_details_success_response(self, user_dto):
        pass

    def mobile_number_already_registered_response(self, mobile_number):
        pass

    def username_already_taken_response(self, username):
        pass

    def weak_password_exception_response(self):
        pass
