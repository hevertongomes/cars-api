from django.urls import include, path
from rest_framework import routers
from cars import views

default_version='v0'

router = routers.DefaultRouter()
router.register(r'marcas', views.MarcaViewSet)
router.register(r'carros', views.CarroViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]