import uuid

from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_user_details_dto(data):
    from restaurant.interactors.storages.dtos import AddUserDetailsDTO

    return AddUserDetailsDTO(
        id=str(uuid.uuid4()),
        username=data.get('username'),
        first_name=data.get('first_name'),
        mobile_number=data.get('mobile_number'),
        last_name=data.get('last_name', ''),
        password=data.get('password', ''),
        is_staff=data.get('is_staff', False),
        is_active=False,
    )


@api_view(['POST'])
def sign_up(request):
    from restaurant.serializers.user_serializer import UserSerializer
    from restaurant.storages.user_storage_implementation import UserStorageImplementation
    from restaurant.interactors.sign_up_interactor import AddUserDetailsInteractor
    from restaurant.presenters.presenter_implementation import PresenterImplementation

    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)

    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = AddUserDetailsInteractor(user_storage=user_storage)
    response = interactor.sign_up_wrapper(
        user_details_dto=get_user_details_dto(request.data), presenter=presenter
    )
    return Response(response)