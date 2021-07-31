from django.urls import path
from . import views
from .views import OrderItemListView, OrderItemDetailView, OrderSummaryView, add_to_cart,  complete_order, about_us

urlpatterns = [
    path ( '', views.IndexView.as_view (), name="index" ),
    path ( 'create/', views.ProductCreateView.as_view (), name="create" ),
    path ( 'edit/<int:pk>/', views.ProductUpdateView.as_view (), name="edit" ),
    path ( 'delete/<int:pk>/', views.ProductDeleteView.as_view(), name="delete"),
    path ( 'details/<int:pk>/', views.ProductView.as_view (), name="product" ),
    path('cart/<int:pk>/', add_to_cart, name='cart'),
    path('cart/complete/', complete_order, name='order complete'),
    path('order-summary/', OrderSummaryView.as_view(), name='order summary'),
    path('items/', OrderItemListView.as_view(), name='list items'),
    path('items/<int:pk>', OrderItemDetailView.as_view(), name='details item'),
    path('about/', about_us, name='about us'),


]
