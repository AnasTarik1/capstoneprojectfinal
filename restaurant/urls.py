#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/items', views.MenuItemListView.as_view()),
    path('restaurant/menu/items/create/', views.MenuItemCreateView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]  