from django.urls import path
from . import views
from .views import OrderSummaryView, add_to_cart, complete_order, about_us, contacts, home_page

urlpatterns = [
    path ( '', views.IndexView.as_view (), name="index" ),
    path ( 'home/', home_page, name="home" ),
    path ( 'create/', views.ProductCreateView.as_view (), name="create" ),
    path ( 'edit/<int:pk>/', views.ProductUpdateView.as_view (), name="edit" ),
    path ( 'delete/<int:pk>/', views.ProductDeleteView.as_view(), name="delete"),
    path ( 'details/<int:pk>/', views.ProductView.as_view (), name="product" ),
    path('cart/<int:pk>/', add_to_cart, name='cart'),
    path('cart/complete/', complete_order, name='order complete'),
    path('order-summary/', OrderSummaryView.as_view(), name='order summary'),
    path('about/', about_us, name='about us'),
    path('contacts/', contacts, name='contacts'),


]
