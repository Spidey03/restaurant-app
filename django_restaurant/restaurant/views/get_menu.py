from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_menu(request):

    from restaurant.storages.restaurant_storage_implementation import RestaurantStorageImplementation
    from restaurant.interactors.get_menu_list_interactor import GetMenuInteractor
    from restaurant.presenters.presenter_implementation import PresenterImplementation

    restaurant_storage = RestaurantStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetMenuInteractor(restaurant_storage=restaurant_storage)
    response = interactor.get_menu_wrapper(presenter=presenter)
    return Response(response)
