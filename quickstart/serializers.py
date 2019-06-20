from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Items, SavedItems


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id', 'name', 'type', 'videolink', 'description')

class SavedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedItems
        fields = ('id', 'nr', 'name', 'type', 'videolink', 'description', 'day')