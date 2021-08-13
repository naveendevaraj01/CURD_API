from django.urls import path, include
from . import views as v
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API docs",
      default_version='v1',
      description="API curd",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('dataclass',v.dataformVeiwset,basename='dataclass')
router.register('data',v.dataformGenericVeiwset,basename='datageneric')
router.register('data',v.dataformModelViewset,basename='datamodel')

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('data/', v.name_list),
    path('dataclass/', v.dataformAPIView.as_view()),
    path('datageneric/', v.genericAPIView.as_view()),
    path('detail/<int:id>/', v.name_details),
    path('detailclass/<int:id>/',v.dataformDetails.as_view()),
    path('datageneric/<int:id>/', v.genericAPIView.as_view()),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    path('genericviewset/',include(router.urls)),
    path('genericviewset/<int:pk>',include(router.urls)),
    path('modelviewset/',include(router.urls)),
    path('modelviewset/<int:pk>',include(router.urls)),
]