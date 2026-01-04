from django_bolt import Router

from bolt_api.serializers import ItemSerializer

router = Router(prefix="/items")


# Example with path parameters
@router.get("/{item_id}")
async def get_item(item_id: int, q: str | None = None):
    """Get an item by ID."""
    return {"item_id": item_id, "q": q}


@router.post("/")
async def create_item(item: ItemSerializer):
    """Create a new item."""
    return {"item": item, "created": True}


# FIXME: Root endpoints rendered in API docs, but returns 404
# It works if registered with an empty string
# @router.get("", response_model=list[ItemSerializer])
@router.get("/", response_model=list[ItemSerializer])
async def list_items():
    return [
        {"id": 1, "name": "Sample Item", "price": 100.00},
        {"id": 2, "name": "Another Item", "price": 200.00},
        {"id": 3, "name": "Yet Another Item", "price": 300.00},
    ]
