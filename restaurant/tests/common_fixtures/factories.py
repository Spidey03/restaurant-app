import factory
import factory.fuzzy
from restaurant.interactors.storages.dtos import (
    UserDetailsDTO,
    UserDTO,
    AddUserDetailsDTO,
    LoginUserDTO, ItemDTO, TableOrderDTO, OrderDTO
)


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    first_name = factory.Faker('name')
    username = factory.LazyAttribute(lambda o: o.first_name.lower())


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


class ItemDTOFactory(factory.Factory):
    class Meta:
        model = ItemDTO

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    name = factory.Sequence(lambda n: 'Item %d' % n)
    price = 3000
    description = ''


class TableOrderDTOFactory(factory.Factory):
    class Meta:
        model = TableOrderDTO

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    table_id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    user_id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    order_id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)


class OrderDTOFactory(factory.Factory):
    class Meta:
        model = OrderDTO

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    is_paid = True
    items = []
    amount = 0