from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.item_list, name='item_list'),
]

"""
from django.urls import path
from .views import ItemListView

app_name = 'myapp'

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
]

"""
