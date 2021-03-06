import factory
import factory.fuzzy

from restaurant.models import User, Item, Table, Restaurant, Order, TableOrder


class UserModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    first_name = factory.Faker('name')
    last_name = factory.Sequence(lambda n: 'User Last Name %d' % n)
    username = factory.LazyAttribute(lambda o: o.first_name.lower())
    date_joined = factory.Faker('date_time')
    mobile_number = factory.Sequence(lambda n: '9676767%03d' % n)


class ItemModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    name = factory.Faker('name')
    description = factory.Sequence(lambda n: 'Description %d' % n)
    price = 300.0


class RestaurantModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Restaurant

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    name = factory.Faker('name')


class TableModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Table

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    restaurant = factory.SubFactory(RestaurantModelFactory)


class OrderModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    is_paid = False
    amount = 3000


class TableOrderModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TableOrder

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    table = factory.SubFactory(TableModelFactory)
    user = factory.SubFactory(UserModelFactory)
    order = factory.SubFactory(OrderModelFactory)
