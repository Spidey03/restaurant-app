from typing import List

from restaurant.constants.constants import StatusCode
from restaurant.interactors.presenters.presenter_interface import PresenterInterface
from restaurant.interactors.storages.dtos import UserDetailsDTO, ItemDTO


class PresenterImplementation(PresenterInterface):
    def add_user_details_success_response(self, user_dto: UserDetailsDTO):
        return {
            'user_id': user_dto.id,
            'username': user_dto.username,
            'first_name': user_dto.first_name,
            'last_name': user_dto.last_name,
            'mobile_number': user_dto.mobile_number
        }

    def mobile_number_already_registered_response(self, mobile_number):
        from restaurant.constants.exception_message import MOBILE_NUMBER_ALREADY_EXIST

        response = MOBILE_NUMBER_ALREADY_EXIST[0].format(mobile_number)
        res_status = MOBILE_NUMBER_ALREADY_EXIST[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def username_already_taken_response(self, username):
        from restaurant.constants.exception_message import USERNAME_ALREADY_TAKEN_EXCEPTION

        response = USERNAME_ALREADY_TAKEN_EXCEPTION[0].format(username)
        res_status = USERNAME_ALREADY_TAKEN_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def weak_password_exception_response(self):
        from restaurant.constants.exception_message import WEAK_PASSWORD_EXCEPTION

        response = WEAK_PASSWORD_EXCEPTION[0]
        res_status = WEAK_PASSWORD_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def username_not_found_response(self, username):
        from restaurant.constants.exception_message import USERNAME_NOT_FOUND

        response = USERNAME_NOT_FOUND[0].format(username)
        res_status = USERNAME_NOT_FOUND[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def login_failed_response(self):
        from restaurant.constants.exception_message import LOGIN_FAILED

        response = LOGIN_FAILED[0]
        res_status = LOGIN_FAILED[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def login_successful_response(self, auth_token_dto):
        return {
            'user_id': auth_token_dto.user_id,
            'access_token': auth_token_dto.access_token,
            'refresh_token': auth_token_dto.refresh_token,
            'expires': auth_token_dto.expires,
        }

    def get_menu_items_response(self, menu_items_dto_list: List[ItemDTO]):
        return [
            {
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'price': item.price
            } for item in menu_items_dto_list
        ]

    def order_created_successfully(self, order_id: str):
        from restaurant.constants.exception_message import ORDER_CREATE_SUCCESSFULLY

        response = ORDER_CREATE_SUCCESSFULLY[0].format(order_id)
        res_status = ORDER_CREATE_SUCCESSFULLY[1]
        http_status_code = StatusCode.Created_Success.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def table_not_found_response(self, table_id: str):
        from restaurant.constants.exception_message import TABLE_NOT_FOUND

        response = TABLE_NOT_FOUND[0].format(table_id)
        res_status = TABLE_NOT_FOUND[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def items_not_found(self, item_ids: List[str]):
        from restaurant.constants.exception_message import SELECTED_ITEMS_NOT_FOUND

        response = SELECTED_ITEMS_NOT_FOUND[0].format(item_ids)
        res_status = SELECTED_ITEMS_NOT_FOUND[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }
