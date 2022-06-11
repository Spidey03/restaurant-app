import factory
import factory.fuzzy

from restaurant.models import User, Item


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
