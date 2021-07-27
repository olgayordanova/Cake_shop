from django.urls import path
from . import views
from .views import OrderCreateView, OrderItemCreateView, OrderItemListView, OrderItemDetailView, OrderListView, \
    add_to_cart

urlpatterns = [
    path ( '', views.IndexView.as_view (), name="index" ),
    path ( 'create/', views.ProductCreateView.as_view (), name="create" ),
    path ( 'edit/<int:pk>/', views.ProductUpdateView.as_view (), name="edit" ),
    path ( 'delete/<int:pk>/', views.ProductDeleteView.as_view(), name="delete"),
    path ( 'details/<int:pk>/', views.ProductView.as_view (), name="product" ),

    path('cart/<int:pk>/', add_to_cart, name='cart'),
    path('orders/create/', OrderCreateView.as_view(), name='create order'),
    path('items/', OrderItemListView.as_view(), name='list items'),
    path('items/<int:pk>', OrderItemDetailView.as_view(), name='details item'),
    path('items/create/', OrderItemCreateView.as_view(), name='create item'),

]
