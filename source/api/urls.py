from django.urls import include, path
from rest_framework import routers
from api import views
from api.views import RateView

router = routers.DefaultRouter()

router.register(r'comments', views.CommentViewSet)
router.register(r'photos', views.PhotoViewSet)


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('rate/<int:pk>/', RateView.as_view())
]