from random import randrange


def items_payload_factory() -> dict[str, str]:
    return {
        "name": "Item " + str(randrange(1, 20)),
        "height": str(randrange(1, 15)),
        "width": str(randrange(1, 15)),
        "weight": str(randrange(1, 15))
    }


def items_updated_payload_factory(item_id) -> dict[str, str]:
    return {
        "id": item_id,
        "name": "Item " + str(randrange(1, 20)),
        "height": str(randrange(1, 15)),
        "width": str(randrange(1, 15)),
        "weight": str(randrange(1, 15))
    }
