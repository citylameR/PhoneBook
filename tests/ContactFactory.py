from db.models.contacts import Contact

import factory


class ContactFactory(factory.Factory):
    class Meta:
        model = Contact

    first_name = factory.Faker('first_name', locale='ru_RU')
    last_name = factory.Faker('last_name', locale='ru_RU')
    middle_name = factory.Faker('middle_name', locale='ru_RU')
    company = factory.Faker('company', locale='ru_RU')
    work_phone = factory.Faker('phone_number', locale='ru_RU')
    personal_phone = factory.Faker('phone_number', locale='ru_RU')
