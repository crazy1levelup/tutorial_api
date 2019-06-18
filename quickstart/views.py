from django.contrib.auth.models import User, Group
from rest_framework import viewsets
# from .serializers import UserSerializer, GroupSerializer
from .models import Items, SavedItems
from .serializers import ItemsSerializer, SavedItemsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SavedItemsFilter, ItemsFilter

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    filter_class = ItemsFilter
    ordering_fields = '__all__'

class SavedItemsViewSet(viewsets.ModelViewSet):
    queryset = SavedItems.objects.all()
    serializer_class = SavedItemsSerializer
    filter_class = SavedItemsFilter
    ordering_fields = '__all__'


# @api_view(['GET', 'POST'])
# def item_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         items = Items.objects.all()
#         serializer = ItemsSerializer(items, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ItemsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def item_detail(request, pk, format=None):
#     try:
#         items = Items.objects.get(pk=pk)
#     except Items.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ItemsSerializer(items)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ItemsSerializer(items, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method =='DELETE':
#         items.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)