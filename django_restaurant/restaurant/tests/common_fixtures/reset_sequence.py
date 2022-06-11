def reset():
    reset_model_factories()
    reset_dto_factories()


def reset_model_factories():
    from restaurant.tests.common_fixtures.model_factories import (
        UserModelFactory,
    )

    UserModelFactory.reset_sequence(0)


def reset_dto_factories():
    from restaurant.tests.common_fixtures.factories import (
        UserDTOFactory,
        UserDetailsDTOFactory,
        AddUserDetailsDTOFactory,
        LoginUserDTOFactory,
    )

    UserDTOFactory.reset_sequence(0)
    UserDetailsDTOFactory.reset_sequence(0, force=True)
    AddUserDetailsDTOFactory.reset_sequence(0, force=True)
    LoginUserDTOFactory.reset_sequence(0)
