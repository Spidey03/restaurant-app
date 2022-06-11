def reset():
    reset_model_factories()
    reset_dto_factories()


def reset_model_factories():
    from restaurant.tests.common_fixtures.model_factories import (
        UserModelFactory, ItemModelFactory, TableModelFactory,
        RestaurantModelFactory, OrderModelFactory
    )

    UserModelFactory.reset_sequence(0)
    ItemModelFactory.reset_sequence(0)
    RestaurantModelFactory.reset_sequence(0)
    TableModelFactory.reset_sequence(0)
    OrderModelFactory.reset_sequence(0)


def reset_dto_factories():
    from restaurant.tests.common_fixtures.factories import (
        UserDTOFactory,
        UserDetailsDTOFactory,
        AddUserDetailsDTOFactory,
        LoginUserDTOFactory,
        ItemDTOFactory
    )

    UserDTOFactory.reset_sequence(0)
    UserDetailsDTOFactory.reset_sequence(0, force=True)
    AddUserDetailsDTOFactory.reset_sequence(0, force=True)
    LoginUserDTOFactory.reset_sequence(0)
    ItemDTOFactory.reset_sequence(0)
