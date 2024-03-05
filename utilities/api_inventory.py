from random import randrange


def inventory_payload_factory(item_id, deposit_id) -> dict[str, str]:
    return {
        "item_id": item_id,
        "deposit_id": deposit_id,
        "item_count": randrange(1, 15)
    }


def inventory_updated_payload_factory(item_id, deposit_id, inventory_id) -> dict[str, str]:
    return {
        "id": inventory_id,
        "item_id": item_id,
        "deposit_id": deposit_id,
        "item_count": randrange(1, 15)
    }
