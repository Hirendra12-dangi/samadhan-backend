from django.urls import path,include
from rest_framework import routers
from .views import ReportViewSet

router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]