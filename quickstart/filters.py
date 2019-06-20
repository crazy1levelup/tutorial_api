import django_filters
from .models import SavedItems, Items

class SavedItemsFilter(django_filters.FilterSet):
    class Meta:
        model = SavedItems
        fields = {
            'nr': ['exact'],
            'type': ['exact'],
            'day': ['exact'],
        }

class ItemsFilter(django_filters.FilterSet):
    class Meta:
        model = Items
        fields = {
            'type': ['exact'],
        }