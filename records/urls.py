from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecordViewSet, summary_view

router = DefaultRouter()
router.register('records', RecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', summary_view),
]