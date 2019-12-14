from django.urls import path, include
from .views import IndexClass, DetailedView, ChangeView, PhotoDeleteView, PhotoCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexClass.as_view(), name='index_url'),
    path('details/<int:pk>/', DetailedView.as_view(), name='details_url'),
    path('update/<int:pk>/', ChangeView.as_view(), name='change_url'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='delete_url'),
    path('create/', PhotoCreateView.as_view(), name='create_url'),
    path('accounts/', include('django.contrib.auth.urls'))
]
