from rest_framework import serializers

from .models import Item, List


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "is_on_chest"]


class ListSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSerializer(many=True)

    class Meta:
        model = List
        fields = ["id", "name", "user", "url", "item_set"]
