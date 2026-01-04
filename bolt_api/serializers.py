from django_bolt.serializers import Serializer


class ItemSerializer(Serializer):
    id: int
    name: str
    price: float
