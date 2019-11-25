from django.urls import path
from .views import test_response, nowy_film, edytuj_film, usun_film

from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('test/', test_response, name="test_response"),
    path('new/', nowy_film, name="nowy_film"),
    path('edytuj/<int:id>/', edytuj_film, name="edytuj_film"),
    path('usun/<int:id>/', usun_film, name="usun_film"),
    path('', include(router.urls))
]