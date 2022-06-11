from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response


@login_required
@api_view(['GET'])
def get_order(request):
    from restaurant.storages.restaurant_storage_implementation import RestaurantStorageImplementation
    from restaurant.storages.user_storage_implementation import UserStorageImplementation
    from restaurant.interactors.get_order_details import GetOrderInteractor
    from restaurant.presenters.presenter_implementation import PresenterImplementation

    restaurant_storage = RestaurantStorageImplementation()
    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    user_id = str(request.user.id)
    order_id = request.data.get('order_id')

    interactor = GetOrderInteractor(
        restaurant_storage=restaurant_storage,
        user_storage=user_storage
    )
    response = interactor.get_order_details_wrapper(
        user_id=user_id, order_id=order_id, presenter=presenter
    )
    return Response(response)
