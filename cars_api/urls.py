from django.urls import include, path
from rest_framework import routers
from cars import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


default_version='v1'

schema_view = get_schema_view(
    openapi.Info(
        title='Cars API',
        default_version=default_version,
        description='API para gerenciar veículos',
        terms_of_service='https://www.google.com/policies/terms',           # editar para termos reais
        contact=openapi.Contact(email='heverton.gomes2018@gmail.com'),
        license=openapi.License(name='HEV LICENSE'),                  # editar para licença real
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


router = routers.DefaultRouter()
router.register(r'marcas', views.MarcaViewSet)
router.register(r'carros', views.CarroViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(f'api/{default_version}/swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger'),
    path(f'api/{default_version}/redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),
    path(f'api/{default_version}/', include(router.urls)),
]