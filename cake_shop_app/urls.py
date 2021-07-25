
from django.urls import path
from . import views

urlpatterns = [
    path ( '', views.IndexView.as_view (), name="index" ),
    path ( 'create/', views.ProductCreateView.as_view (), name="create" ),
    path ( 'edit/<int:pk>/', views.ProductUpdateView.as_view (), name="edit" ),
    path ( 'details/<int:pk>/', views.ProductView.as_view (), name="product" ),
    # path('', views.index, name="index"),
    # path('create/', views.create, name="create"),
]