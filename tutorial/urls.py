"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from quickstart import views
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'items', views.ItemsViewSet)
router.register(r'saveditems', views.SavedItemsViewSet)

urlpatterns =[
        path('', include(router.urls))
    ]

# urlpatternss = [
# path('items/', views.item_list),
#         path('items/<int:pk>', views.item_detail),
# ]
# urlpatternss = format_suffix_patterns(urlpatternss)