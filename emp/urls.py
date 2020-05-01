from rest_framework import routers
from .views import ExecutiveViewSet, ManagerViewSet, ExecLeaveRequestViewSet, LeaveBalanceViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('executive', ExecutiveViewSet, basename='executive')
router.register('manager', ManagerViewSet, basename='manager')
router.register('execleave', ExecLeaveRequestViewSet, basename='execleave')
router.register('leavebalance', LeaveBalanceViewSet, basename='leavebalance')

urlpatterns = [
    path('', include(router.urls)),
]
