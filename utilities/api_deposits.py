from faker import Faker


def deposits_payload_factory() -> dict[str, str]:
    fake = Faker('pt_BR')
    return {
        "name": fake.name(),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.estado_sigla(),
        "zipcode": fake.postcode()
    }


def deposits_updated_payload_factory(deposit_id) -> dict[str, str]:
    fake = Faker('pt_BR')
    return {
        "id": deposit_id,
        "name": fake.name(),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.estado_sigla(),
        "zipcode": fake.postcode()
    }
