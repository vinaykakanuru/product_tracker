from django.urls import path
from link.views import home, DeleteProductView, update_items

urlpatterns = [
    path('', home, name='home'),
    path('update/', update_items, name='update-view'),
    path('delete/<pk>/', DeleteProductView.as_view(), name='delete-item'),
]
