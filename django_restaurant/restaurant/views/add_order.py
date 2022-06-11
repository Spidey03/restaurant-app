from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response


@login_required()
@api_view(['POST'])
def add_order(request):
    from restaurant.storages.restaurant_storage_implementation import RestaurantStorageImplementation
    from restaurant.interactors.create_order_interactor import CreateOrderInteractor
    from restaurant.presenters.presenter_implementation import PresenterImplementation

    restaurant_storage = RestaurantStorageImplementation()
    presenter = PresenterImplementation()

    user_id = request.user.id
    table_id = request.data.get('table_id')
    items = request.data.get('items')

    interactor = CreateOrderInteractor(restaurant_storage=restaurant_storage)
    response = interactor.create_order_wrapper(
        user_id=user_id, table_id=table_id, items=items, presenter=presenter
    )
    return Response(response)
