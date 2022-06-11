from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_login_user_details_dto(data):
    from restaurant.interactors.storages.dtos import LoginUserDTO

    return LoginUserDTO(
        username=data.get('username'),
        password=data.get('password', ''),
    )


@api_view(['POST'])
def login(request):
    from restaurant.storages.user_storage_implementation import UserStorageImplementation
    from restaurant.interactors.login_interactor import LoginInteractor
    from restaurant.presenters.presenter_implementation import PresenterImplementation

    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    login_user_dto = get_login_user_details_dto(request.data)
    interactor = LoginInteractor(user_storage=user_storage)
    response = interactor.login_wrapper(
        login_user_dto=login_user_dto, presenter=presenter
    )
    return Response(response)