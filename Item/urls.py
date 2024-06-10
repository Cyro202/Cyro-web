# urls.py in the Item app
from django.urls import path

from . import views

app_name = 'Item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new', views.new, name='new'),
    path('item/<int:item_id>/', views.item_detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
