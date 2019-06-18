import django_filters
from .models import SavedItems

class SavedItemsFilter(django_filters.FilterSet):
    class Meta:
        model = SavedItems
        fields = {
            'nr': ['exact'],
            'type': ['exact'],
        }