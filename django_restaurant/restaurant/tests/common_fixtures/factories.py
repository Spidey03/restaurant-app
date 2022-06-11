import factory
import factory.fuzzy
from restaurant.interactors.storages.dtos import (
    UserDetailsDTO,
    UserDTO,
    AddUserDetailsDTO,
    LoginUserDTO
)


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    first_name = factory.Faker('name')
    username = factory.LazyAttribute(lambda o: o.first_name.lower())
    email = factory.LazyAttribute(
        lambda o: f"{o.first_name.replace(' ', '').lower()}@gmail.com"
    )


class UserDetailsDTOFactory(UserDTOFactory):
    class Meta:
        model = UserDetailsDTO

    last_name = factory.Sequence(lambda n: 'User Last Name %d' % n)
    date_joined = str(factory.Faker('date_time'))
    mobile_number = factory.Sequence(lambda n: '9676767%03d' % n)


class AddUserDetailsDTOFactory(UserDTOFactory):
    class Meta:
        model = AddUserDetailsDTO

    password = factory.Sequence(lambda n: 'password%d' % n)
    is_staff = False
    is_active = False
    last_name = factory.Sequence(lambda n: 'User Last Name %d' % n)
    date_joined = str(factory.Faker('date_time'))
    mobile_number = factory.Sequence(lambda n: '9676767%03d' % n)


class LoginUserDTOFactory(factory.Factory):
    class Meta:
        model = LoginUserDTO

    username = factory.Faker('name')
    password = factory.Sequence(lambda n: 'password%d' % n)